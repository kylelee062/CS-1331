def thingy(s):
    maxL = 0
    curL = 1

    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            curL += 1
        else:
            maxL = max(maxL, curL)
            curL = 1
    maxL = max(maxL, curL)
    print(maxL)
    return maxL
boom = str(input("WORDS:"))
thingy(boom)