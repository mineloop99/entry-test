import pytest
from scripts.meta.model import EModel
from scripts.process.search_method import submit_search
from scripts.utils.data_init import data_init

data = data_init()


@pytest.mark.order1
def test_search_ticket_by_id():
    ticket_id = "de70eb6b-0717-40f9-9322-75f1262cda12"
    user_name_true = "Geneva Poole"
    res_list = submit_search(EModel.Tickets, "_id", ticket_id, data)
    assert user_name_true == res_list[ticket_id]["submitter_name"]
