import os
from cryptography.fernet import Fernet

BASE_PATH = "Memory"

def get_entity_path(entity):

    path = os.path.join(BASE_PATH, entity)

    if not os.path.exists(path):
        os.makedirs(path)

    return path


def generate_key(entity):

    key = Fernet.generate_key()

    path = get_entity_path(entity)

    with open(os.path.join(path, "key.key"), "wb") as f:
        f.write(key)

    return key


def load_key(entity):

    path = get_entity_path(entity)

    key_path = os.path.join(path, "key.key")

    if not os.path.exists(key_path):
        return generate_key(entity)

    with open(key_path, "rb") as f:
        return f.read()


def encrypt(entity, data):

    key = load_key(entity)

    f = Fernet(key)

    return f.encrypt(data.encode())


def decrypt(entity, data):

    key = load_key(entity)

    f = Fernet(key)

    return f.decrypt(data).decode()


def store_reflection(entity, text):

    path = get_entity_path(entity)

    encrypted = encrypt(entity, text)

    with open(os.path.join(path, "reflections.enc"), "ab") as f:
        f.write(encrypted + b"\n")


def load_entity_memory(entity):

    path = get_entity_path(entity)

    file_path = os.path.join(path, "reflections.enc")

    if not os.path.exists(file_path):
        return "No memory yet."

    key = load_key(entity)

    f = Fernet(key)

    reflections = []

    with open(file_path, "rb") as file:

        for line in file:

            try:
                reflections.append(f.decrypt(line.strip()).decode())
            except:
                pass

    return "\n".join(reflections[-10:])
