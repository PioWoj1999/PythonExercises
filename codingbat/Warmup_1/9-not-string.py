# Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged.
def not_string(str):
    if len(str) < 3:
        return "not " + str
    elif str[0:3] == "not":
        return str
    else:
        return "not " + str
