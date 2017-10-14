import re


def count_str(string, sub):
    return len(re.findall('(?=(' + sub + '))', string))


if __name__ == '__main__':
    print(count_str('azcbobobegghakl', 'bob') == 2)
