from enum import Enum


class YesNo(str, Enum):
    Yes = "yes"
    No = "no"


class UserStatus(str, Enum):
    Enabled = "enabled"
    Disabled = "disabled"


class UserRole(str, Enum):
    Player = "player"
    Admin = "admin"
    Bot = "bot"
