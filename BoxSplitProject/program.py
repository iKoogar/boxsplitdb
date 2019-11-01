import data.mongo_setup as mongo_setup

import services.data_service as svc


def main(): 
    mongo_setup.global_init()

    split = svc.create_split("split0", "test", 5)
    box = svc.find_box_by_id("5dbc721062df01eed0940b06")
    user = svc.find_user_by_email("poog@split.box")
    user.boxes.append(box)
    box.splits.append(split)







if __name__ == '__main__':
    main()