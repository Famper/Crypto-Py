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
    print("Original: {o}\nCrypto: {cr}\nResult: {r}\n".format(
        o=text,
        cr=Info(num),
        r=res
        ))
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
    print("Original: {o}\nCrypto: {cr}\nResult: {r}\n".format(
        o=text,
        cr=Info(num),
        r=res
        ))
    return res


def Check_Argv(text, type, num):
    type, num, b_type, b_num = Check_Def_Arg(type, num)

    if (b_type is False or b_num is False):
        return (type, num, False)

    print("Length: {num} symbols".format(num=len(text)))

    return (type, int(num), True)


def Info(num):
    find = {
        0: "ROT1",
        1: "ROT13",
        2: "ROT24"
    }
    return find[num]


def Check_Def_Arg(type, num):
    lists = [
        'def',
        'enc',
        'dec'
    ]

    nums = [
        'def',
        '0',
        '1',
        '2'
    ]

    for let in lists:
        if (str(type) == let):
            b_type = True
            break
        else:
            b_type = False

    if (str(type) == 'def'):
        type = str('enc')

    for let in nums:
        if (str(num) == let):
            b_num = True
            break
        else:
            b_num = False

    if (str(num) == 'def'):
        num = int(0)

    return (type, num, b_type, b_num)
