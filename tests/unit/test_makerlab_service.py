import pytest
from unittest.mock import Mock
from src.makerlab_service import MakerLabService


def make_service():
    tool_repository = Mock()
    member_repository = Mock()
    checkout_repository = Mock()
    queue_repository = Mock()
    service = MakerLabService(
        tool_repository,
        member_repository,
        checkout_repository,
        queue_repository,
    )
    return service, tool_repository, member_repository, checkout_repository, queue_repository


def test_checkout_tool_raises_when_parameters_are_missing():
    service, *_ = make_service()
    with pytest.raises(ValueError, match="Member ID and tool ID are required"):
        service.checkout_tool(None, 1)


def test_checkout_tool_returns_false_when_member_does_not_exist():
    service, _, member_repository, _, _ = make_service()
    member_repository.exists.return_value = False
    assert service.checkout_tool(999, 1) is False


def test_checkout_tool_creates_checkout_when_all_rules_are_satisfied():
    service, tool_repository, member_repository, checkout_repository, queue_repository = make_service()

    member_repository.exists.return_value = True
    tool_repository.exists.return_value = True
    member_repository.is_blocked.return_value = False
    member_repository.has_required_training.return_value = True
    tool_repository.is_available.return_value = True
    checkout_repository.count_active_checkouts.return_value = 0
    queue_repository.next_member.return_value = None
    queue_repository.has_queue_entry.return_value = False

    result = service.checkout_tool(10, 1)

    assert result is True
    tool_repository.mark_unavailable.assert_called_once_with(1)
    checkout_repository.create_checkout.assert_called_once_with(10, 1)


def test_return_tool_returns_false_when_checkout_does_not_exist():
    service, _, _, checkout_repository, _ = make_service()
    checkout_repository.is_tool_with_member.return_value = False
    assert service.return_tool(10, 1) is False


def test_join_queue_adds_member_when_rules_are_satisfied():
    service, tool_repository, member_repository, checkout_repository, queue_repository = make_service()

    member_repository.exists.return_value = True
    tool_repository.exists.return_value = True
    member_repository.is_blocked.return_value = False
    member_repository.has_required_training.return_value = True
    tool_repository.is_available.return_value = False
    queue_repository.has_queue_entry.return_value = False
    checkout_repository.is_tool_with_member.return_value = False

    result = service.join_queue(10, 1)

    assert result is True
    queue_repository.add_to_queue.assert_called_once_with(10, 1)


def test_join_queue_raises_when_parameters_are_missing():
    service, *_ = make_service()
    with pytest.raises(ValueError, match="Member ID and tool ID are required"):
        service.join_queue(None, 1)
