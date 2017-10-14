def substrfun(s):
    index = 1
    smax = ''
    ssub = s[0]
    while index < len(s) - 1:
        while index < len(s) - 1 and s[index - 1] <= s[index]:
            ssub += s[index]
            index += 1
        else:
            if len(ssub) > len(smax):
                (ssub, smax) = (smax, ssub)
            ssub = s[index]
        index += 1
    return smax


if __name__ == '__main__':
    print(substrfun('abcbcd') == 'abc')
    print(substrfun('azcbobobegghakl') == 'beggh')
