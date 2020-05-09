import sys, os
sys.path.append("modules/")
import main

main.Check_Argv(sys.argv[1])

if (sys.argv[2].lower() == "enc" and (int(sys.argv[3]) >= 0 and int(sys.argv[3]) <= 2)):
    main.Crypto_Encode(sys.argv[1], int(sys.argv[3]))
elif (sys.argv[2].lower() == "dec" and (int(sys.argv[3]) >= 0 and int(sys.argv[3]) <= 2)):
    main.Crypto_Decode(sys.argv[1], int(sys.argv[3]))
else:
    print("Error: Non-Value")
