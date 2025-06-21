def is_palindrom(my_str):
    if len(my_str) <= 1:
        return True
    if my_str[0] != my_str[-1]:
        return False
    return is_palindrom(my_str[1: -1])
