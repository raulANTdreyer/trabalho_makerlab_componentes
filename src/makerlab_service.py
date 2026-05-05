class MakerLabService:
    def __init__(self, tool_repository, member_repository, checkout_repository, queue_repository):
        self.tool_repository = tool_repository
        self.member_repository = member_repository
        self.checkout_repository = checkout_repository
        self.queue_repository = queue_repository

    def checkout_tool(self, member_id: int, tool_id: int) -> bool:
        if not member_id or not tool_id:
            raise ValueError("Member ID and tool ID are required")

        if not self.member_repository.exists(member_id):
            return False

        if not self.tool_repository.exists(tool_id):
            return False

        if self.member_repository.is_blocked(member_id):
            return False

        if not self.member_repository.has_required_training(member_id):
            return False

        if not self.tool_repository.is_available(tool_id):
            return False

        if self.checkout_repository.count_active_checkouts(member_id) >= 2:
            return False

        next_member = self.queue_repository.next_member(tool_id)
        if next_member is not None and next_member != member_id:
            return False

        self.tool_repository.mark_unavailable(tool_id)
        self.checkout_repository.create_checkout(member_id, tool_id)

        if self.queue_repository.has_queue_entry(member_id, tool_id):
            self.queue_repository.remove_from_queue(member_id, tool_id)

        return True

    def return_tool(self, member_id: int, tool_id: int) -> bool:
        if not member_id or not tool_id:
            raise ValueError("Member ID and tool ID are required")

        if not self.checkout_repository.is_tool_with_member(member_id, tool_id):
            return False

        self.checkout_repository.close_checkout(member_id, tool_id)

        if not self.queue_repository.has_any_queue(tool_id):
            self.tool_repository.mark_available(tool_id)

        return True

    def join_queue(self, member_id: int, tool_id: int) -> bool:
        if not member_id or not tool_id:
            raise ValueError("Member ID and tool ID are required")

        if not self.member_repository.exists(member_id):
            return False

        if not self.tool_repository.exists(tool_id):
            return False

        if self.member_repository.is_blocked(member_id):
            return False

        if not self.member_repository.has_required_training(member_id):
            return False

        if self.tool_repository.is_available(tool_id):
            return False

        if self.queue_repository.has_queue_entry(member_id, tool_id):
            return False

        if self.checkout_repository.is_tool_with_member(member_id, tool_id):
            return False

        self.queue_repository.add_to_queue(member_id, tool_id)
        return True
