import sys, random, string

def Crypto_Encode(text):
    res = ["rot1", "rot13", "rot24"]
    rot1 = str.maketrans(
        "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789",
        "BCDEFGHIJKLMNOPQRSTUVWXYZAbcdefghijklmnopqrstuvwxyza1234567890"
    )
    rot13 = str.maketrans(
        "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789",
        "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm3456789012"
    )
    rot24 = str.maketrans(
        "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789",
        "YZABCDEFGHIJKLMNOPQRSTUVWXyzabcdefghijklmnopqrstuvwx4567890123"
    )
    enc = random.randint(0, 2)
    print("Crypto: {r}".format(r = res[enc]))
    if (enc == 0):
        print("Result: {r}\n".format(r = str.translate(text, rot1)))
        return (str.translate(text, rot1))
    elif (enc == 1):
        print("Result: {r}\n".format(r = str.translate(text, rot13)))
        return (str.translate(text, rot13))
    elif (enc == 2):
        print("Result: {r}\n".format(r = str.translate(text, rot24)))
        return (str.translate(text, rot24))
    return text

def Check_Argv():
    res = ''
    i = (-1)
    for let in sys.argv: i += 1
    while (i > 0):
        res += sys.argv[i]
        i -= 1
    print('Result: {r}'.format(r = len(res)))

    return res
