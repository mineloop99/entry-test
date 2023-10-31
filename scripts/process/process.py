import json
from scripts.process.search_method import submit_search
from scripts.validator.user_input import (
    field_input_val,
    model_input_val,
    search_input_val,
)


def search_options():
    print("Type 'quit' to exit at any time, Press 'Enter' to continue")
    print(
        "Select search options: \n  * Press 1 to search \n  * Press 2 to view a list of searchable fields \n * Type 'quit' to exit"
    )
    print("Type 'quit' to exit at any time, Press 'Enter' to continue")

    while True:
        search_num = input()
        if search_input_val(search_num):
            return search_num
        else:
            print("Value not found please type again")


def type_search_opstions():
    print("Select 1) Users or 2) Tickets or 3) Organizations: ")
    while True:
        model_num = input()
        if model_input_val(model_num):
            return model_num
        else:
            print("Value not found please type again")


def field_select_search_opstions(dict: dict):
    print("Enter search term: ")
    while True:
        field = input()
        if field_input_val(field, dict):
            return field
        else:
            print("Value not found please type again")


def view_searchable_options(
    user_data: dict, ticket_data: dict, organization_data: dict
):
    print("All fields can be search: ")
    print("--------------------------------------------")
    print("Search Users With: ")
    for key in user_data:
        print(key)
    print("--------------------------------------------")
    print("Search Tickets With: ")
    for key in ticket_data:
        print(key)
    print("--------------------------------------------")
    print("Search Organizations With: ")
    for key in organization_data:
        print(key)


def do_searching_for(search_num: str, key: str, data: dict):
    value = input("Enter value: ")
    print("Searching for", key, "with a value of: ", value)
    res_list = submit_search(search_num, key, value, data)
    if len(res_list) == 0:
        print("The record not found : ")
    # printing result
    else:
        print("The result found : ")
        for value in res_list:
            print(json.dumps(res_list[value], indent=2))
