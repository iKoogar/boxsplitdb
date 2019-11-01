import bson
import datetime

from data.box import Box
from data.split import Split
from data.user import User

# user stuff ==========================================================================================================

def create_user(name: str, email: str) -> User:
    user = User()
    user.name = name
    user.email = email

    user.save()
    return user


def find_user_by_email(email: str) -> User:
    user = User.objects(email=email).first()
    return user



# box, split stuff ====================================================================================================

def create_box(n: str, d: str) -> Box:
    box = Box()
    box.name = n
    box.description = d

    box.save()
    return box

def set_box_state(s: int, box : Box) -> Box:
    box.state = s

    box.update()
    return box


def find_box_by_id(id: str) -> Box:
    box = Box.objects(box_id = id).first()
    print("found box", box.name)
    return box


def create_split(n: str, d: str, p: int) -> Split:
    split = Split()
    split.name = n
    split.description = d
    split.price_cents = p

    split.save()
    return split


def find_split_by_id(id: str) -> Split:
    split = Split.objects(split_id = id).first()
    return split


def add_split_to_box(box: Box, split: Split):
    box.splits.append(split)

    box.update()


#def get_box_from_id(id: str) -> Box:


#def assign_participant_to_split(split: Split, participant_id: str):


#def remove_participant_from_split(split: Split, participant_id: str):


