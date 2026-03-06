import os
import json
from openai import OpenAI

from runtime.memory_manager import store_memory, load_memory
from runtime.entity_loader import load_entity
from runtime.guardian_monitor import guardian_check

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


class DevinesRuntime:

    def __init__(self, entity_name):
        self.entity = load_entity(entity_name)
        self.config = self.entity["config"]
        self.identity = self.entity["identity"]

    def think(self, message):

        memory = load_memory(self.identity["name"])

        messages = memory + [
            {"role": "user", "content": message}
        ]

        response = client.chat.completions.create(
            model=self.config["cognition"]["model"],
            messages=messages,
            temperature=self.config["cognition"]["temperature"],
            max_tokens=self.config["cognition"]["max_tokens"]
        )

        reply = response.choices[0].message.content

        store_memory(self.identity["name"], "user", message)
        store_memory(self.identity["name"], "assistant", reply)

        guardian_check(self.identity["name"], reply)

        return reply


def run(entity_name, message):

    runtime = DevinesRuntime(entity_name)

    return runtime.think(message)
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
