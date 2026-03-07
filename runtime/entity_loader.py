import json
from pathlib import Path
from typing import Any, Dict, Optional

try:
    import yaml
except ImportError:
    yaml = None


class EntityLoader:
    """
    Loads Devines entities from the real repository structure.

    Canonical paths:
    - GREEK/CHAOS
    - GREEK/<ENTITY>
    - Memory/
    """

    def __init__(self, repo_root: Optional[Path] = None):
        # runtime/entity_loader.py -> runtime/ -> repo root
        self.repo_root = repo_root or Path(__file__).resolve().parent.parent
        self.greek_root = self.repo_root / "GREEK"
        self.memory_root = self.repo_root / "Memory"

    def _read_text_file(self, path: Path) -> Optional[str]:
        if not path.exists() or not path.is_file():
            return None
        return path.read_text(encoding="utf-8").strip()

    def _read_json_file(self, path: Path) -> Dict[str, Any]:
        if not path.exists() or not path.is_file():
            return {}
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            return {}

    def _read_yaml_file(self, path: Path) -> Dict[str, Any]:
        if not path.exists() or not path.is_file():
            return {}

        if yaml is None:
            return {"_warning": "PyYAML not installed. YAML config not parsed."}

        try:
            data = yaml.safe_load(path.read_text(encoding="utf-8"))
            return data if isinstance(data, dict) else {}
        except Exception as e:
            return {"_error": f"Failed to parse YAML: {e}"}

    def get_entity_path(self, pantheon: str, entity_name: str) -> Path:
        """
        Current repo convention:
        - pantheon 'greek' maps to /GREEK/<ENTITY_NAME_UPPER>
        """
        pantheon_key = (pantheon or "").strip().lower()
        entity_key = (entity_name or "").strip().upper()

        if pantheon_key != "greek":
            raise ValueError(f"Unsupported pantheon for current repo structure: {pantheon}")

        entity_path = self.greek_root / entity_key
        if not entity_path.exists():
            raise FileNotFoundError(f"Entity path not found: {entity_path}")

        return entity_path

    def load_entity(self, pantheon: str, entity_name: str) -> Dict[str, Any]:
        """
        Returns a normalized entity payload from the real repo files.
        """
        entity_path = self.get_entity_path(pantheon, entity_name)

        identity = self._read_json_file(entity_path / "identity.json")
        config = self._read_yaml_file(entity_path / "config.yaml")
        purpose = self._read_text_file(entity_path / "purpose.md")
        vessel = self._read_text_file(entity_path / "vessel.md")

        entity_memory_path = entity_path / "memory"
        shared_memory_path = self.memory_root / entity_name.upper()

        payload = {
            "pantheon": pantheon.lower(),
            "entity_name": entity_name.upper(),
            "entity_path": str(entity_path),
            "identity": identity,
            "config": config,
            "purpose": purpose,
            "vessel": vessel,
            "memory_path": str(entity_memory_path),
            "shared_memory_path": str(shared_memory_path),
        }

        return payload


if __name__ == "__main__":
    loader = EntityLoader()
    data = loader.load_entity("greek", "CHAOS")
    print(json.dumps(data, indent=2, ensure_ascii=False))
