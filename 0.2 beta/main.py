import commands

DIGITS = ["1","2","3","4","5","6","7","8","9","0"]

print("Jeenani assistant version 0.2.0 Beta")

while True:
    comm = input("")
    assistant = commands.talkBack()

    if(comm == "math" or comm == "Math"):
        nu1 = input("   first number: ")
        oppo = input("   operator: ")
        nu2 = input("   second number: ")

        try:
            nu1 = int(nu1)
            nu2 = int(nu2)
            if(oppo == '+'):
                print(nu1 + nu2)
            elif(oppo == '-'):
                print(nu1 - nu2)
            elif(oppo == '*' or oppo == 'x'):
                print(nu1 * nu2)
            elif(oppo == '/'):
                print(nu1 / nu2)
            else:
                print("the operator is invalid")
        except:
            print("given number is invalid")

    elif(comm == "quit"): break
    else: print(assistant.talk(comm))

print("bye sir/miss")    
    