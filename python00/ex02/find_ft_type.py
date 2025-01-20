def all_thing_is_obj(object: any) -> int:
    if isinstance (object, (list, tuple, set, dict, str)):
        if isinstance (object, str):
            print(f'{object} is in the kitchen : {type(object)}')
        else:
            if type(object) == list:
                print(f'List : ', end='')
            elif type(object) == tuple:
                print(f'Tuple : ', end='')
            elif type(object) == set:
                print(f'Set : ', end='')
            elif type(object) == dict:
                print(f'Dictionary : ', end='')
            print(type(object))
    else:
        print('Type not found')
    return 42
