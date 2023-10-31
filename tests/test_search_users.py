import pytest
from scripts.meta.model import EModel
from scripts.process.search_method import submit_search
from scripts.utils.data_init import data_init

data = data_init()


@pytest.mark.order1
def test_search_users_by_id():
    uid = 71
    ticket_0 = "A Catastrophe in Micronesia"
    res_list = submit_search(EModel.Users, "_id", str(uid), data)
    assert res_list[uid]["ticket_0"] == ticket_0
