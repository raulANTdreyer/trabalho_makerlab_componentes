import pytest
from src.tool_repository import ToolRepository


def test_exists_returns_true_for_existing_tool():
    repo = ToolRepository()
    assert repo.exists(1) is True


def test_is_available_returns_true_for_available_tool():
    repo = ToolRepository()
    assert repo.is_available(1) is True


def test_is_available_returns_false_for_unavailable_tool():
    repo = ToolRepository()
    assert repo.is_available(3) is False


def test_mark_unavailable_changes_tool_state():
    repo = ToolRepository()
    repo.mark_unavailable(1)
    assert repo.is_available(1) is False


def test_mark_available_changes_tool_state():
    repo = ToolRepository()
    repo.mark_available(3)
    assert repo.is_available(3) is True


def test_mark_unavailable_raises_for_unknown_tool():
    repo = ToolRepository()
    with pytest.raises(ValueError, match="Tool not found"):
        repo.mark_unavailable(999)
