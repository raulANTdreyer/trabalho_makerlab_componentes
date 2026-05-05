class QueueRepository:
    def __init__(self):
        self._queue = []

    def add_to_queue(self, member_id: int, tool_id: int) -> None:
        self._queue.append({"member_id": member_id, "tool_id": tool_id})

    def has_queue_entry(self, member_id: int, tool_id: int) -> bool:
        return any(
            entry["member_id"] == member_id and entry["tool_id"] == tool_id
            for entry in self._queue
        )

    def has_any_queue(self, tool_id: int) -> bool:
        return any(entry["tool_id"] == tool_id for entry in self._queue)

    def next_member(self, tool_id: int):
        for entry in self._queue:
            if entry["tool_id"] == tool_id:
                return entry["member_id"]
        return None

    def remove_from_queue(self, member_id: int, tool_id: int) -> None:
        for entry in list(self._queue):
            if entry["member_id"] == member_id and entry["tool_id"] == tool_id:
                self._queue.remove(entry)
                return
        raise ValueError("Queue entry not found")
