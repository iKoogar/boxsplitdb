import bson
import datetime

from data.box import Box
from data.split import Split
from data.user import User

# user stuff ==========================================================================================================

def create_account(name: str, email: str) -> User:
    user = User()
    user.name = name
    user.email = email

    user.save()
    return user


def find_account_by_email(email: str) -> User:
    user = User.objects(email=email).first()
    return user

# box, split stuff ====================================================================================================

def create_box(id: str, n: str, d: str) -> Box:
    box = Box()
    box.leader_user_id = id
    box.name = n
    box.description = d

    box.save()
    return box

def set_box_state(s: int, box : Box):
    box.state = s

    box.save()
    return box

#def add_split_to_box(split: Split):


#def get_box_from_id(id: str) -> Box:


#def assign_participant_to_split(split: Split, participant_id: str):


#def remove_participant_from_split(split: Split, participant_id: str):


