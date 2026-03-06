import os
import yaml


class GuardianManager:

    def __init__(self, entity_path):
        self.entity_path = entity_path
        self.guardians = {}

        self.load_guardians()

    def load_guardians(self):
        """
        Load guardian configuration from entity config
        """

        config_path = os.path.join(self.entity_path, "config.yaml")

        if not os.path.exists(config_path):
            print("No guardian config found")
            return

        with open(config_path, "r") as f:
            config = yaml.safe_load(f)

        guardians = config.get("guardians", [])

        for guardian in guardians:
            name = guardian.get("name")
            role = guardian.get("role")

            self.guardians[name] = {
                "role": role,
                "status": "active"
            }

    def list_guardians(self):

        return list(self.guardians.keys())

    def get_guardian(self, name):

        return self.guardians.get(name)

    def guardian_status(self, name):

        guardian = self.guardians.get(name)

        if guardian:
            return guardian["status"]

        return "unknown"
