# Given a string, return a new string where the first and last chars have been exchanged.
def front_back(str):
    if len(str) < 2:
        return str
    else:
        new_str = str[len(str) - 1] + str[1 : len(str) - 1] + str[0]
        return new_str
