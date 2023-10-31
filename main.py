from scripts.meta.model import EModel, ESearchValue
from scripts.process.process import (
    do_searching_for,
    field_select_search_opstions,
    search_options,
    type_search_opstions,
    view_searchable_options,
)
from scripts.utils.data_init import data_init

data = data_init()


def main():
    step = 1
    search_num = ""
    single_data_model = None
    field_name = ""
    while step != 0:
        match (step):
            case 1:
                search = search_options()
                if search is ESearchValue.ViewOptions.value:
                    view_searchable_options(
                        data[EModel.Users][0],
                        data[EModel.Tickets][0],
                        data[EModel.Organizations][0],
                    )
                step += 1
            case 2:
                search_num = type_search_opstions()
                single_data_model = data[EModel(search_num)]
                step += 1
            case 3:
                field_name = field_select_search_opstions(single_data_model[0])
                step += 1
            case 4:
                do_searching_for(search_num, field_name, data)
                step = 0
            case _:
                step = 1


main()
