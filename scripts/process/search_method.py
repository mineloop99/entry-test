from scripts.meta.model import EModel


def searching_user(
    key: str, value: str, user_data: list, ticket_data: list, org_data: list
):
    print("User Search: ...")
    res_list = {}
    # find user_data
    for sub in user_data:
        if type(sub[key]) != "list":
            if str(sub[key]) == value:
                res_list[sub["_id"]] = sub
                # find organization if user found
                if "organization_id" in sub:
                    for org_sub in org_data:
                        if sub["organization_id"] == org_sub["_id"]:
                            res_list[sub["_id"]]["organization_name"] = org_sub["name"]
        elif value in sub[key]:
            res_list[sub["_id"]] = sub

    # find in ticket
    ticket_count = 0
    for sub in ticket_data:
        if "submitter_id" in sub and sub["submitter_id"] in res_list:
            res_list[sub["submitter_id"]]["ticket_" + str(ticket_count)] = sub[
                "subject"
            ]
            ticket_count += 1
        elif "assignee_id" in sub and sub["assignee_id"] in res_list:
            res_list[sub["assignee_id"]]["ticket_" + str(ticket_count)] = sub["subject"]
            ticket_count += 1

    return res_list


def searching_ticket(
    key: str, value: str, user_data: list, ticket_data: list, org_data: list
):
    print("Ticket Search: ...")
    res_list = {}
    # find ticket_data
    for sub in ticket_data:
        if type(sub[key]) != "list":
            if str(sub[key]) == value:
                res_list[sub["_id"]] = sub
                # find organization if ticket found
                if "organization_id" in sub:
                    for org_sub in org_data:
                        if sub["organization_id"] == org_sub["_id"]:
                            res_list[sub["_id"]]["organization_name"] = org_sub["name"]
                for user_sub in user_data:
                    if "submitter_id" in sub and sub["submitter_id"] == user_sub["_id"]:
                        res_list[sub["_id"]]["submitter_name"] = user_sub["name"]
                    if "assignee_id" in sub and sub["assignee_id"] == user_sub["_id"]:
                        res_list[sub["_id"]]["assignee_name"] = user_sub["name"]
        elif value in sub[key]:
            res_list[sub["_id"]] = sub

    return res_list


def searching_organization(
    key: str, value: str, user_data: list, ticket_data: list, org_data: list
):
    print("Organization Search: ...")
    res_list = {}
    # find org_data
    for sub in org_data:
        if type(sub[key]) != "list":
            if str(sub[key]) == value:
                res_list[sub["_id"]] = sub
        elif value in sub[key]:
            res_list[sub["_id"]] = sub
    # find in user_data
    user_name_count = 0
    for sub in user_data:
        if "organization_id" in sub and sub["organization_id"] in res_list:
            res_list[sub["organization_id"]]["user_name_" + str(user_name_count)] = sub[
                "name"
            ]
            user_name_count += 1
    # find ticket_data
    ticket_count = 0
    for sub in ticket_data:
        if "organization_id" in sub and sub["organization_id"] in res_list:
            res_list[sub["organization_id"]][
                "ticket_subject_" + str(ticket_count)
            ] = sub["subject"]
            ticket_count += 1
    return res_list


def submit_search(search_num: str, key: str, value: str, data: dict):
    match (EModel(search_num)):
        case EModel.Users:
            return searching_user(
                key,
                value,
                data[EModel.Users],
                data[EModel.Tickets],
                data[EModel.Organizations],
            )
        case EModel.Tickets:
            return searching_ticket(
                key,
                value,
                data[EModel.Users],
                data[EModel.Tickets],
                data[EModel.Organizations],
            )
        case EModel.Organizations:
            return searching_organization(
                key,
                value,
                data[EModel.Users],
                data[EModel.Tickets],
                data[EModel.Organizations],
            )
