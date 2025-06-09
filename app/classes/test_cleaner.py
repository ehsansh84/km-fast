from publics import db, Settings
from bson import ObjectId
from tests.dummy_data import Dummy
Settings.DB_NAME = Settings.DB_NAME_TEST

col_user = db()['user']
col_sample = db()['sample']

class TestCleaner:
    @staticmethod
    def init_users():
        col_user.update_one({"_id": ObjectId(Dummy.Player.PLAYER1_ID)}, {"$set": Dummy.Player.PLAYER_1}, upsert=True)
        col_user.update_one({"_id": ObjectId(Dummy.Player.PLAYER2_ID)}, {"$set": Dummy.Player.PLAYER_2}, upsert=True)
        col_user.update_one({"_id": ObjectId(Dummy.Player.PLAYER3_ID)}, {"$set": Dummy.Player.PLAYER_3}, upsert=True)
        col_user.update_one({"_id": ObjectId(Dummy.Player.ADMIN_ID)}, {"$set": Dummy.Player.PLAYER_ADMIN}, upsert=True)
        col_user.delete_many({"username": {'$in':Dummy.Player.NEW_USERS}})


    @staticmethod
    def clear_test_samples():
        col_sample.delete_many({'$or': [{"player1_id": {'$in':[Dummy.Player.PLAYER1_ID,Dummy.Player.PLAYER2_ID]}},
                                        {"player2_id": {'$in':[Dummy.Player.PLAYER1_ID,Dummy.Player.PLAYER2_ID]}}]})
