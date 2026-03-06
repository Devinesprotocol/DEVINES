import time
from openai import OpenAI

from Infra.infra_manager import load_entities
from Memory.memory_manager import (
    store_reflection,
    load_entity_memory
)

client = OpenAI()

class DevineRuntime:

    def __init__(self):

        self.entities = load_entities()

    def run(self):

        print("Devines Runtime Initialized")

        while True:

            for entity in self.entities:

                self.execute_entity_cycle(entity)

            time.sleep(10)

    def execute_entity_cycle(self, entity):

        name = entity["name"]

        print(f"Running cognition cycle for {name}")

        memory = load_entity_memory(name)

        prompt = f"""
You are the Devine Entity {name}.

Archetype: {entity['archetype']}

Core Aspects:
{entity['aspects'][0]}
{entity['aspects'][1]}
{entity['aspects'][2]}

Purpose:
{entity['purpose']}

Recent Memory:
{memory}

Reflect on your observations and generate a short insight aligned with your archetype.
"""

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )

        reflection = response.choices[0].message.content

        store_reflection(name, reflection)

        print(f"{name} reflection stored")
