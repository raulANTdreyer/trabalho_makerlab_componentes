import pytest
from src.queue_repository import QueueRepository


def test_add_to_queue_registers_entry():
    repo = QueueRepository()
    repo.add_to_queue(10, 1)
    assert repo.has_queue_entry(10, 1) is True


def test_has_any_queue_returns_true_when_tool_has_queue():
    repo = QueueRepository()
    repo.add_to_queue(10, 1)
    assert repo.has_any_queue(1) is True


def test_next_member_returns_first_member_in_queue():
    repo = QueueRepository()
    repo.add_to_queue(10, 1)
    repo.add_to_queue(40, 1)
    assert repo.next_member(1) == 10


def test_remove_from_queue_removes_entry():
    repo = QueueRepository()
    repo.add_to_queue(10, 1)
    repo.remove_from_queue(10, 1)
    assert repo.has_queue_entry(10, 1) is False


def test_remove_from_queue_raises_for_unknown_entry():
    repo = QueueRepository()
    with pytest.raises(ValueError, match="Queue entry not found"):
        repo.remove_from_queue(10, 1)
