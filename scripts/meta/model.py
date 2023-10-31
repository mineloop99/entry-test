import enum


class ESearchValue(enum.Enum):
    Search = "1"
    ViewOptions = "2"
    Quit = "quit"


class EModel(enum.Enum):
    Users = "1"
    Tickets = "2"
    Organizations = "3"
