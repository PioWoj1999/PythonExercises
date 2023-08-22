# Given a non-empty string like "Code" return a string like "CCoCodCode".
def string_splosion(str):
    new_str = ""
    for i in range(1, len(str)):
        new_str += str[0:i]
    return new_str + str
