import sys
import main

if (len(sys.argv) < 4):
    print('Error: No Arguments\n')
    exit()

type, num, check = main.Check_Argv(sys.argv[1], sys.argv[2], sys.argv[3])

if (check is False):
    print('Error: Wrong Arguments\n')
    exit()

if (type == 'enc'):
    main.Crypto_Encode(sys.argv[1], num)
else:
    main.Crypto_Decode(sys.argv[1], num)
