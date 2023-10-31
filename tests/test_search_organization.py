import pytest
from scripts.meta.model import EModel
from scripts.process.search_method import submit_search
from scripts.utils.data_init import data_init

data = data_init()


@pytest.mark.order1
def test_search_organization_by_id():
    org_id = 123
    user_name_0 = "Josefa Mcfadden"
    res_list = submit_search(EModel.Organizations, "_id", str(org_id), data)
    assert user_name_0 == res_list[org_id]["user_name_0"]
