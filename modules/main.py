import sys, random, string

def Crypto_Encode(text, num):
    rots = {
        0: str.maketrans(
            "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789",
            "BCDEFGHIJKLMNOPQRSTUVWXYZAbcdefghijklmnopqrstuvwxyza1234567890"
            ),
        1: str.maketrans(
            "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789",
            "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm3456789012"
            ),
        2: str.maketrans(
            "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789",
            "YZABCDEFGHIJKLMNOPQRSTUVWXyzabcdefghijklmnopqrstuvwx4567890123"
            )
    }

    res = str.translate(text, rots[num])
    print("Original: {o}\nCrypto: {cr}\nResult: {r}\n".format(o = text, cr = Info(num), r = res))
    return res

def Crypto_Decode(text, num):
    rots = {
        0: str.maketrans(
            "BCDEFGHIJKLMNOPQRSTUVWXYZAbcdefghijklmnopqrstuvwxyza1234567890",
            "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
            ),
        1: str.maketrans(
            "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm3456789012",
            "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
            ),
        2: str.maketrans(
            "YZABCDEFGHIJKLMNOPQRSTUVWXyzabcdefghijklmnopqrstuvwx4567890123",
            "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
            )
    }

    res = str.translate(text, rots[num])
    print("Original: {o}\nCrypto: {cr}\nResult: {r}\n".format(o = text, cr = Info(num), r = res))
    return res

def Check_Argv(text):
    return print("Length: {l} symbols".format(l = len(text)))

def Info(num):
    find = {
        0: "ROT1",
        1: "ROT13",
        2: "ROT24"
    }
    return find[num]
