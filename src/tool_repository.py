class ToolRepository:
    def __init__(self):
        self._tools = {
            1: {"name": "Impressora 3D", "available": True},
            2: {"name": "Cortadora a Laser", "available": True},
            3: {"name": "Estação de Solda", "available": False},
        }

    def exists(self, tool_id: int) -> bool:
        return tool_id in self._tools

    def is_available(self, tool_id: int) -> bool:
        if tool_id not in self._tools:
            return False
        return self._tools[tool_id]["available"]

    def mark_unavailable(self, tool_id: int) -> None:
        if tool_id not in self._tools:
            raise ValueError("Tool not found")
        self._tools[tool_id]["available"] = False

    def mark_available(self, tool_id: int) -> None:
        if tool_id not in self._tools:
            raise ValueError("Tool not found")
        self._tools[tool_id]["available"] = True
