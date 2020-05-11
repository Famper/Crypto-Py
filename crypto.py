import sys
import main

type, check = main.Check_Argv(sys.argv[1], sys.argv[2], int(sys.argv[3]))

if (type == 'enc'):
    main.Crypto_Encode(sys.argv[1], int(sys.argv[3]))
else:
    main.Crypto_Decode(sys.argv[1], int(sys.argv[3]))
