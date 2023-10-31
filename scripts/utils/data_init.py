from scripts.meta.model import EModel
from scripts.utils.json import json_load


def data_init():
    return {
        EModel.Users: json_load("data/users.json"),
        EModel.Tickets: json_load("data/tickets.json"),
        EModel.Organizations: json_load("data/organizations.json"),
    }
