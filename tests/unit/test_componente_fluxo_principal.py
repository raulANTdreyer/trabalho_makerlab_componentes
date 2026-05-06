import pytest
from src.makerlab_service import MakerLabService
from src.checkout_repository import CheckoutRepository
from src.member_repository import MemberRepository
from src.queue_repository import QueueRepository
from src. tool_repository import ToolRepository

def test_fluxo_componente () :
    checkout_repo = CheckoutRepository ()
    tool_repo = CheckoutRepository ()
    member_repo = CheckoutRepository ()
    queue_repo = CheckoutRepository ()

    member_repo.exists = lambda *args: True
    member_repo.is_blocked = lambda *args: False
    member_repo.has_required_training = lambda *args: True
    tool_repo.exists = lambda *args: True
    tool_repo.is_available = lambda *args: True
    tool_repo.mark_unavailable = lambda *args: None
    queue_repo.has_queue_entry = lambda *args: False
    queue_repo.next_member = lambda *args: None
    checkout_repo.count_active_checkouts = lambda *args: 0
    

    service = MakerLabService( tool_repo , member_repo, checkout_repo, queue_repo )

    member_id = 9
    tool_id = 5

    sucess = service.checkout_tool( member_id, tool_id )

    if sucess: 
        assert checkout_repo.has_active_checkout( tool_id ) is True
        assert checkout_repo.is_tool_with_member( member_id, tool_id ) is True
        print ("\n [Sucess] não acredito que funcionou")
    else :
        print ("\n [ValueError]")