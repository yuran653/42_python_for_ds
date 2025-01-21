def all_thing_is_obj(object: any) -> int:
    if isinstance(object, (list, tuple, set, dict, str)):
        if isinstance(object, str):
            print(f'{object} is in the kitchen : {type(object)}')
        else:
            if type(object) is list:
                print('List : ', end='')
            elif type(object) is tuple:
                print('Tuple : ', end='')
            elif type(object) is set:
                print('Set : ', end='')
            elif type(object) is dict:
                print('Dictionary : ', end='')
            print(type(object))
    else:
        print('Type not found')
    return 42
