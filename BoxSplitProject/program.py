import data.mongo_setup as mongo_setup

import services.data_service as svc


def main(): 
    mongo_setup.global_init()
    box = svc.create_box('5db31f89e67f49d5bf0bf2bd', 'box1', 'test')
    svc.set_box_state(1, box)



if __name__ == '__main__':
    main()