import sys
sys.path.append("modules/")
import main

Text = ''

Text = main.Check_Argv()
main.Crypto_Encode(Text)
