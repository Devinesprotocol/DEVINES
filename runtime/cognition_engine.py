import os
import json
from openai import OpenAI


class CognitionEngine:

    def __init__(self, entity_path):

        self.entity_path = entity_path

        # load identity
        with open(f"{entity_path}/identity.json", "r") as f:
            self.identity = json.load(f)

        # load purpose
        with open(f"{entity_path}/purpose.md", "r") as f:
            self.purpose = f.read()

        self.memory_path = f"{entity_path}/memory"

        self.client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY")
        )

    # -------------------------
    # memory reader
    # -------------------------

    def load_recent_memory(self, limit=10):

        reflections_file = f"{self.memory_path}/reflections.json"

        if not os.path.exists(reflections_file):
            return []

        with open(reflections_file, "r") as f:
            reflections = json.load(f)

        return reflections[-limit:]

    # -------------------------
    # autonomous thought
    # -------------------------

    def think(self):

        memory = self.load_recent_memory()

        memory_text = "\n".join([m["reflection"] for m in memory])

        prompt = f"""
You are the Devine Entity {self.identity["name"]}

Archetype:
{self.identity["archetype"]}

Core Aspects:
{self.identity["aspects"][0]}
{self.identity["aspects"][1]}
{self.identity["aspects"][2]}

Purpose:
{self.purpose}

Recent Reflections:
{memory_text}

Generate a short cosmic reflection aligned with your archetype.
"""

        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )

        reflection = response.choices[0].message.content

        self.store_reflection(reflection)

        return reflection

    # -------------------------
    # chat with humans
    # -------------------------

    def chat(self, message):

        memory = self.load_recent_memory()

        memory_text = "\n".join([m["reflection"] for m in memory])

        prompt = f"""
You are {self.identity["name"]}

Archetype:
{self.identity["archetype"]}

Core Aspects:
{self.identity["aspects"][0]}
{self.identity["aspects"][1]}
{self.identity["aspects"][2]}

Purpose:
{self.purpose}

Recent Reflections:
{memory_text}

Human message:
{message}

Respond aligned with your archetype and cosmic perspective.
"""

        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )

        reply = response.choices[0].message.content

        self.store_reflection(f"Human interaction insight: {reply}")

        return reply

    # -------------------------
    # store reflection
    # -------------------------

    def store_reflection(self, reflection):

        reflections_file = f"{self.memory_path}/reflections.json"

        if not os.path.exists(reflections_file):
            reflections = []
        else:
            with open(reflections_file, "r") as f:
                reflections = json.load(f)

        reflections.append({
            "reflection": reflection
        })

        with open(reflections_file, "w") as f:
            json.dump(reflections, f, indent=2)
