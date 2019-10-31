import data.mongo_setup as mongo_setup

import services.data_service as svc


def main(): 
    mongo_setup.global_init()
    #split = create_split("split0", "test", 5)
    user = svc.find_account_by_email("poog@split.box")
    print(user.name)




if __name__ == '__main__':
    main()