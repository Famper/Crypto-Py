import sys
sys.path.append("modules/")
import main

main.Check_Argv(sys.argv[1])

if (sys.argv[2].lower() == "enc"):
    main.Crypto_Encode(sys.argv[1], sys.argv[3])
elif (sys.argv[2].lower() == "dec"):
    main.Crypto_Decode(sys.argv[1], sys.argv[3])
else:
    print("Error: Non-Value")
