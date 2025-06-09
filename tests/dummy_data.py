from bson import ObjectId
from datetime import datetime
from copy import deepcopy
from app.db_models.consts import YesNo
from app.db_models.consts import UserRole


class Dummy:
    WRONG_ID = '678d08cad22f2ef005ae4cad'
    
    class Player:
        PLAYER1_ID = "67c305c441c5e3e35fd6944e"
        PLAYER2_ID = "67c09b8f0d1fd5cd34a13ad5"
        PLAYER3_ID = "68021b7dc569ac332ec2b048"
        ADMIN_ID = "67fb9e6b3760be6cecdbc8d9"

        PLAYER_DOC = {
            "ip": "192.168.0.231",
            "country": "Unknown",
            "region": "Unknown",
            "isp": "Unknown",
            "name": "",
            "family": "",
            "email": "",
            "country_code": "",
            "mobile": "",
            "password": "",
            "avatar": "",
            "last_login": datetime.now(),
            "status": "enabled",
            "email_verified": False,
            "mobile_verified": False,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        }

        PLAYER_1 = {
            "_id": ObjectId(PLAYER1_ID),  # Add or override specific fields
            "username": "test_player1",
            "role": UserRole.Player,
            **deepcopy(PLAYER_DOC),  # Inherit all fields from PLAYER_DOC
        }

        PLAYER_2 = {
            "_id": ObjectId(PLAYER2_ID),  # Add or override specific fields
            "username": "test_player2",
            "role": UserRole.Player,
            **deepcopy(PLAYER_DOC),  # Inherit all fields from PLAYER_DOC
        }

        PLAYER_3 = {
            "_id": ObjectId(PLAYER3_ID),  # Add or override specific fields
            "username": "test_player3",
            "role": UserRole.Player,
            **deepcopy(PLAYER_DOC),  # Inherit all fields from PLAYER_DOC
        }

        PLAYER_ADMIN = {
            "_id": ObjectId(ADMIN_ID),  # Add or override specific fields
            "username": "admin",
            "role": UserRole.Admin,
            **deepcopy(PLAYER_DOC),  # Inherit all fields from PLAYER_DOC
        }

        NEW_USERS = ['new_user1', 'new_user2', 'new_user3']
