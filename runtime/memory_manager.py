import os
import json


BASE_MEMORY = "memory"


def memory_path(entity):

    path = os.path.join(BASE_MEMORY, entity)

    if not os.path.exists(path):
        os.makedirs(path)

    return os.path.join(path, "memory.json")


def load_memory(entity):

    path = memory_path(entity)

    if not os.path.exists(path):
        return []

    with open(path) as f:
        return json.load(f)


def store_memory(entity, role, content):

    path = memory_path(entity)

    memory = []

    if os.path.exists(path):
        with open(path) as f:
            memory = json.load(f)

    memory.append({
        "role": role,
        "content": content
    })

    with open(path, "w") as f:
        json.dump(memory, f, indent=2)
