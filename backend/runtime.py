"""
DEVINES PROTOCOL
Runtime Engine

The Runtime is responsible for executing the cognition loop
of all Devine Entities inside the Devines Protocol.

This system coordinates:

• Entity cognition cycles
• Memory persistence
• Guardian monitoring
• Broadcast communication
• System integrity checks
"""

import time
import logging

from memory_manager import MemoryManager
from infra_manager import InfraManager


class DevinesRuntime:

    def __init__(self):

        self.entities = {}
        self.memory = MemoryManager()
        self.infra = InfraManager()

        logging.basicConfig(level=logging.INFO)

    # ---------------------------------------
    # Entity Registration
    # ---------------------------------------

    def register_entity(self, entity):

        self.entities[entity.name] = entity
        logging.info(f"Entity registered: {entity.name}")

    # ---------------------------------------
    # Cognition Loop
    # ---------------------------------------

    def run_entity_cycle(self, entity):

        logging.info(f"Running cognition cycle for {entity.name}")

        try:

            perception = entity.observe()

            reasoning = entity.think(perception)

            self.memory.store(entity.name, reasoning)

            reflection = entity.reflect()

            entity.update_state(reflection)

            entity.broadcast_if_relevant()

        except Exception as e:

            logging.error(f"Runtime error for {entity.name}: {str(e)}")

    # ---------------------------------------
    # Guardian Monitoring
    # ---------------------------------------

    def guardian_evaluation(self, entity):

        """
        Placeholder for Guardian System integration.
        Each guardian evaluates the entity behavior.
        """

        logging.info(f"Guardian evaluation triggered for {entity.name}")

    # ---------------------------------------
    # Main Runtime Loop
    # ---------------------------------------

    def start(self):

        logging.info("Devines Protocol Runtime Started")

        while True:

            for entity in self.entities.values():

                self.run_entity_cycle(entity)

                self.guardian_evaluation(entity)

            time.sleep(10)
