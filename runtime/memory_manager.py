import os
import json
from cryptography.fernet import Fernet

class MemoryManager:

    def __init__(self, entity_path):

        self.entity_path = entity_path
        self.memory_path = f"{entity_path}/memory"

        if not os.path.exists(self.memory_path):
            os.makedirs(self.memory_path)

        self.key_path = f"{entity_path}/memory.key"

        if not os.path.exists(self.key_path):
            key = Fernet.generate_key()
            with open(self.key_path, "wb") as f:
                f.write(key)

        with open(self.key_path, "rb") as f:
            self.key = f.read()

        self.cipher = Fernet(self.key)

    def store_reflection(self, text):

        encrypted = self.cipher.encrypt(text.encode())

        filename = f"{self.memory_path}/reflection_{len(os.listdir(self.memory_path))}.enc"

        with open(filename, "wb") as f:
            f.write(encrypted)

    def load_recent_memory(self, limit=5):

        files = sorted(os.listdir(self.memory_path))[-limit:]

        memories = []

        for file in files:

            with open(f"{self.memory_path}/{file}", "rb") as f:

                encrypted = f.read()
                decrypted = self.cipher.decrypt(encrypted).decode()

                memories.append(decrypted)

        return "\n".join(memories)            memory = json.load(f)

    memory.append({
        "role": role,
        "content": content
    })

    with open(path, "w") as f:
        json.dump(memory, f, indent=2)
