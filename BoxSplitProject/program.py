import data.mongo_setup as mongo_setup

import services.data_service as svc


def main(): 
    mongo_setup.global_init()

    split = svc.find_split_by_id("5dbc8670e3e74473175d283e")
    box = svc.find_box_by_id("5dbc8670e3e74473175d283e")
    user = svc.find_user_by_email("poog@split.box")

    print(box.name)

    user.boxes.append(box)
    box.splits.append(split)

    user.save()
    box.save()






if __name__ == '__main__':
    main()