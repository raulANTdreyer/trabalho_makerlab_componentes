class CheckoutRepository:
    def __init__(self):
        self._active_checkouts = []

    def create_checkout(self, member_id: int, tool_id: int) -> None:
        self._active_checkouts.append({"member_id": member_id, "tool_id": tool_id})

    def has_active_checkout(self, tool_id: int) -> bool:
        return any(checkout["tool_id"] == tool_id for checkout in self._active_checkouts)

    def is_tool_with_member(self, member_id: int, tool_id: int) -> bool:
        return any(
            checkout["member_id"] == member_id and checkout["tool_id"] == tool_id
            for checkout in self._active_checkouts
        )

    def count_active_checkouts(self, member_id: int) -> int:
        return sum(1 for checkout in self._active_checkouts if checkout["member_id"] == member_id)

    def close_checkout(self, member_id: int, tool_id: int) -> None:
        for checkout in list(self._active_checkouts):
            if checkout["member_id"] == member_id and checkout["tool_id"] == tool_id:
                self._active_checkouts.remove(checkout)
                return
        raise ValueError("Active checkout not found")
