import sys
sys.path.append("modules/")
import main

Text = ''

def Check_Argv():
    res = ''
    all = 0
    i = (-1)
    for let in sys.argv: i += 1
    while (i > 0):
        res += sys.argv[i]
        all += len(sys.argv[i])
        i -= 1
    print('Result: {r}'.format(r = all))

    return res

Text = Check_Argv()
main.Crypto_Encode(Text)
