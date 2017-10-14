import re


def remove_not_alpha_num(string):
    return re.sub('[^0-9a-zA-Z]+', '', string)


if __name__ == '__main__':
    print(remove_not_alpha_num('a000 aa-b') == 'a000aab')
