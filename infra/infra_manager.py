import json
import os

ENTITIES_PATH = "Entities"


def load_entities():

    entities = []

    for root, dirs, files in os.walk(ENTITIES_PATH):

        for file in files:

            if file == "identity.json":

                path = os.path.join(root, file)

                with open(path) as f:

                    entity = json.load(f)

                    entities.append(entity)

    return entities
