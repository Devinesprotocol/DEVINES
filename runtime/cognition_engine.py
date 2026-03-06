import datetime


class CognitionEngine:
    """
    Core cognition layer for a Devine entity.

    Responsibilities:
    - Receive user input
    - Route thinking to guardians
    - Store reflections in memory
    - Update knowledge graph
    """

    def __init__(self, guardian_manager, memory_manager, knowledge_graph):
        self.guardian_manager = guardian_manager
        self.memory_manager = memory_manager
        self.knowledge_graph = knowledge_graph

    def process_input(self, entity_name, user_input):
        """
        Main cognition pipeline.
        """

        # Step 1 — select guardian
        guardian = self.guardian_manager.select_guardian(user_input)

        # Step 2 — guardian reasoning
        response = self.guardian_manager.process_with_guardian(
            guardian,
            user_input
        )

        # Step 3 — store memory reflection
        reflection = {
            "timestamp": datetime.datetime.utcnow().isoformat(),
            "entity": entity_name,
            "guardian": guardian,
            "input": user_input,
            "response": response
        }

        self.memory_manager.store_reflection(entity_name, reflection)

        # Step 4 — update knowledge graph
        self.knowledge_graph.add_interaction(
            entity_name,
            user_input,
            response,
            guardian
        )

        return response
