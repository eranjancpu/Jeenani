import webbrowser

class talkBack:
    def __init__(self):
        # for inputs
        self.HAYou = ["How are you", "how are you", "How are yo", "how are yo", "what's up", "whaUp"]
        self.IAfine = ["I am fine", "i am fine", "I am good", "i am good"]
        self.HDYMade = ["How do you made in", "how do you made in", "What language do you made", "What contry do you made in"]
        self.GTWeb = ["go to the website:", "Go to the website:", "go to web:", "Go to web:"]

        # for outputs 
        self.talkHowAreYou = "I am fine working for 1000 people for the whole world"
        self.talkWhatUp = "Nothing here, just working to 1000 people including you"
        self.talkFine = "Wow, thats good"
        self.talkMade = "I am made in python"
        self.talkMadeContry = "I am made in sri lanka"
        self.GTWout = "ok sir/miss"
        self.noUnder = "sorry, can you please tell me again"
    
    def talk(self, com):
        # for HAYou
        if(com == self.HAYou[0]): return self.talkHowAreYou
        elif(com == self.HAYou[1]): return self.talkHowAreYou
        elif(com == self.HAYou[2]): return self.talkHowAreYou
        elif(com == self.HAYou[3]): return self.talkHowAreYou
        elif(com == self.HAYou[4]): return self.talkWhatUp
        elif(com == self.HAYou[5]): return self.talkWhatUp        
        elif(com == self.IAfine[0]): return self.talkFine # for IAFine
        elif(com == self.IAfine[1]): return self.talkFine
        elif(com == self.IAfine[2]): return self.talkFine
        elif(com == self.IAfine[3]): return self.talkFine
        elif(com == self.HDYMade[0]): return self.talkMade # for HDYMade
        elif(com == self.HDYMade[1]): return self.talkMade
        elif(com == self.HDYMade[2]): return self.talkMade
        elif(com == self.HDYMade[3]): return self.talkMadeContry
        elif(com == self.GTWeb[0]): # for GTWeb
            web = input("What website do you want to go? ")
            webbrowser.open(web)
            return self.GTWout
        elif(com == self.GTWeb[1]):
            web = input("What website do you want to go? ")
            webbrowser.open(web)
            return self.GTWout
        elif(com == self.GTWeb[2]):
            web = input("What website do you want to go? ")
            webbrowser.open(web)
            return self.GTWout
        elif(com == self.GTWeb[3]):
            web = input("What website do you want to go? ")
            webbrowser.open(web)
            return self.GTWout
        else: return self.noUnder
        
