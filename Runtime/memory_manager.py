import os
import json
from cryptography.fernet import Fernet


class MemoryManager:

    def __init__(self, entity_path):

        self.memory_dir = f"{entity_path}/memory"

        if not os.path.exists(self.memory_dir):
            os.makedirs(self.memory_dir)

        self.key_path = f"{self.memory_dir}/memory.key"

        if not os.path.exists(self.key_path):

            key = Fernet.generate_key()

            with open(self.key_path, "wb") as f:
                f.write(key)

        else:

            with open(self.key_path, "rb") as f:
                key = f.read()

        self.cipher = Fernet(key)

        self.memory_file = f"{self.memory_dir}/reflections.enc"

    def store_reflection(self, reflection):

        encrypted = self.cipher.encrypt(reflection.encode())

        with open(self.memory_file, "ab") as f:
            f.write(encrypted + b"\n")

    def load_recent(self, limit=5):

        if not os.path.exists(self.memory_file):
            return "No previous reflections."

        with open(self.memory_file, "rb") as f:
            lines = f.readlines()

        recent = lines[-limit:]

        reflections = []

        for line in recent:

            decrypted = self.cipher.decrypt(line.strip()).decode()

            reflections.append(decrypted)

        return "\n".join(reflections)
