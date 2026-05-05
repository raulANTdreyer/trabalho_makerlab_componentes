class MemberRepository:
    def __init__(self):
        self._members = {
            10: {"name": "Ana", "blocked": False, "trained": True},
            20: {"name": "Bruno", "blocked": True, "trained": True},
            30: {"name": "Carla", "blocked": False, "trained": False},
            40: {"name": "Diego", "blocked": False, "trained": True},
        }

    def exists(self, member_id: int) -> bool:
        return member_id in self._members

    def is_blocked(self, member_id: int) -> bool:
        if member_id not in self._members:
            return False
        return self._members[member_id]["blocked"]

    def has_required_training(self, member_id: int) -> bool:
        if member_id not in self._members:
            return False
        return self._members[member_id]["trained"]
