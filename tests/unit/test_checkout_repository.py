import pytest
from src.checkout_repository import CheckoutRepository


def test_create_checkout_registers_active_checkout():
    repo = CheckoutRepository()
    repo.create_checkout(10, 1)
    assert repo.has_active_checkout(1) is True


def test_count_active_checkouts_counts_only_member_checkouts():
    repo = CheckoutRepository()
    repo.create_checkout(10, 1)
    repo.create_checkout(10, 2)
    repo.create_checkout(40, 3)
    assert repo.count_active_checkouts(10) == 2


def test_is_tool_with_member_returns_true_for_matching_checkout():
    repo = CheckoutRepository()
    repo.create_checkout(10, 1)
    assert repo.is_tool_with_member(10, 1) is True


def test_close_checkout_removes_active_checkout():
    repo = CheckoutRepository()
    repo.create_checkout(10, 1)
    repo.close_checkout(10, 1)
    assert repo.has_active_checkout(1) is False


def test_close_checkout_raises_for_unknown_checkout():
    repo = CheckoutRepository()
    with pytest.raises(ValueError, match="Active checkout not found"):
        repo.close_checkout(10, 1)
