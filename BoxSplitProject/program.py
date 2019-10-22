import BoxSplitProject.data.mongo_setup as mongo_setup

import BoxSplitProject.services.data_service as svc


def main(): 
    mongo_setup.global_init()

    svc.create_account('zachary poo', 'poog@split.box')


if __name__ == '__main__':
    main()