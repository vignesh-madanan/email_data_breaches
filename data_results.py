import tinydb
import time


class DatabaseHandler:
    def __init__(self, user_email_id):
        db = TinyDB('./databases/db.json')
        email_db = db.table('emaildb')

    def set_ids_in_db(self):
        email_db.insert()
    

    def get_ids_from_db(self, user_email_id):
        Email = Query()
        db.search(Email.email == user_email_id)

def get_api_results(self):
    pass
