num = 2
match num:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case 4 | 5:
        print("Four and five")
    case _:
        print("Other number")