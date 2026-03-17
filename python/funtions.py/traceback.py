def level_three():
    print('Lower level starting...')
    return 1 / 0  # This causes a ZeroDivisionError

def level_two():
    level_three()

def level_one():
    level_two()

level_one()