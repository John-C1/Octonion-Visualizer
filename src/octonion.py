"""
Module for octonion math operations.
"""

class Octonion:
    def __init__(self, components):
        if len(components) != 8:
            raise ValueError("An octonion must have 8 components.")
        self.components = list(components)

    def __repr__(self):
        return f"Octonion({self.components})"

    # TODO: Implement octonion multiplication and other operations
