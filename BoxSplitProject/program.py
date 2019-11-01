import data.mongo_setup as mongo_setup

import services.data_service as svc


def main(): 
    mongo_setup.global_init()

    split = svc.create_split("split0", "test", 5)
    box = svc.create_box("box1", "testbox")
    user = svc.create_user("idiot", "poog@split.box")

    user.boxes.append(box)
    box.splits.append(split)
    print (user.boxes)
    print (box.splits)





if __name__ == '__main__':
    main()