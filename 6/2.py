def longest_string(s):
    max_sub = ''
    for i in range(len(s)):
        for j in range(i, len(s)):
            lonest_s = set()
            sub = ''
            for k in range(i, j):
                if s[k] in lonest_s:
                    if len(sub) > len(max_sub):
                        max_sub = sub
                    break
                else:
                    sub += s[k]
                    lonest_s.add(s[k])

    return max_sub


if __name__ == '__main__':
    print(longest_string('abcbcd'))
    print(longest_string('bbbb'))
