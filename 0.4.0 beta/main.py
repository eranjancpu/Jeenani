import commands
import pyttsx3

engine = pyttsx3.init("sapi5")
engine.setProperty("rate", 150)
voice = engine.getProperty("voices")
engine.setProperty('voice', voice[1].id)

outMath = "answer is "

def speak(msg):
    engine.say(msg)
    engine.runAndWait()

DIGITS = ["1","2","3","4","5","6","7","8","9","0"]

print("Jeenani assistant version 0.4.0 Beta")

while True:
    comm = input("")
    assistant = commands.talkBack()

    if(comm == "math" or comm == "Math"):
        speak("   first number: ")
        nu1 = input("   first number ")
        speak("   operator ")
        oppo = input("   operator: ")
        speak("   second number ")
        nu2 = input("   second number: ")

        try:
            nu1 = int(nu1)
            nu2 = int(nu2)
            if(oppo == '+'):
                print(nu1 + nu2)
                speak(f"{outMath}{nu1 + nu2}")
            elif(oppo == '-'):
                print(nu1 - nu2)
                speak(f"{outMath},{nu1 - nu2}")
            elif(oppo == '*' or oppo == 'x'):
                print(nu1 * nu2)
                speak(f"{outMath},{nu1 * nu2}")
            elif(oppo == '/'):
                print(nu1 / nu2)
                speak(f"{outMath}{nu1 / nu2}")
            else:
                speak("the operator is invalid")
        except:
            speak("given number is invalid")

    elif(comm == "quit"): break
    else: speak(assistant.talk(comm))

speak("bye sir/miss")    
    