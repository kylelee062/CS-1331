def get_v2c_ratio(s):
    vowels = "aeiou"
    upperVowels = vowels.upper()
    vCount = 0
    constantCount = 0
    for char in s:
        if char in vowels:
            vCount += 1
        elif char:
            constantCount += 1
    if constantCount == 0:
        ratio = float("infinite") \
            if vCount > 0 \
            else 0.0
    else:
        ratio = vCount / constantCount
    print(f"{ratio:.2f}")
    return ratio

v2cINPUT = str(input("Input words:"))
get_v2c_ratio(v2cINPUT)

