from enum import Enum


class AuthInfo(object):
    def __init__(self, username, access_token):
        self.username = username
        self.access_token = access_token


class Universe(Enum):
    # (id, key)
    # Default = (0, "")  # = Movies
    Movies = (1, "movie")
    Books = (2, "book")
    Games = (3, "videogame")
    TV_Show = (4, "tvshow")
    Comics = (5, "comic")
    Music = (6, "music")


class SubUniverse(Enum):
    Movies = 1
    Books = 2
    Games = 3
    TV_Shows = 4
    Seasons = 5
    Comics = 6
    Albums = 7
    Tracks = 8


class Method(Enum):
    GET = 0
    POST = 1
    PUT = 2
    DELETE = 3


class CurrentUserData(object):
    rating_scout_count = 0.0
    rating_scout_average = 0.0
    wish_scout_count = 0.0


class User(object):
    id = 0
    username = ""
    displayed_name = ""
    first_name = ""
    last_name = ""
    gender_label = None


class Product(object):
    id = 0
    title = ""
    year_of_production = 1970
    release_date = ""
    release_date_stringify = ""
    production_status = ""
    description = ""
    creators = ""
    workers = ""
    genres = ""
    trailers = ""

    # UNIVERSE and SUB-UNIVERSE
    type_id = 0
    subtype_id = 0

    # NOT WORKING ?
    rating = 0.0
    rating_count = 0
    wish_list_count = 0

    # ???
    list_position = None
    list_description = None
    length = 0
    list_item = None
    current_user_data = CurrentUserData()


class List(object):
    id = 0
    title = ""
    description = ""
    date_creation = None
    user = User()

    # UNIVERSE and SUB-UNIVERSE
    type_id = 0
    subtype_id = 0

    # UNKNOWN
    type_label = None
    is_ordered = None
    total_products = None


#
#
#   RESPONSES
#
#


class Response(object):
    code = 0


class SuccessStatusResponse(Response):
    success = False


class PagingStatus(object):
    after = 0
    before = 0


class PagedResponse(Response):
    paging = PagingStatus()


class ProductListResponse(PagedResponse):
    products = [Product()]


class UserInfoResponse(Response, User):
    pass


class ListCreationResponse(SuccessStatusResponse):
    list = List()


class ListInfoResponse(Response, List):
    pass


#
#
#  SEARCH
#
#


class SearchFilter(Enum):
    ALL = "0"
    MOVIES_ONLY = "movies"
    TVSHOWS_ONLY = "tvshows"
    BOOKS_ONLY = "books"
    COMICS_ONLY = "comics"
    GAMES_ONLY = "videogames"
    MUSIC_ALBUM_ONLY = "albums"
    MUSIC_TRACK_ONLY = "tracks"
    LISTS_ONLY = "lists"
    POLLS_ONLY = "polls"
    FRANCHISES_ONLY = "franchises"
    CONTACTS_ONLY = "contacts"
    USERS_ONLY = "users"
    VENUES_ONLY = "venues"


class SearchResponse(PagedResponse):
    products = [Product()]