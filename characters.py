
class Character:

    def __init__(self, name, phrase1, phrase2):
        self.name = name
        self.phrase1 = phrase1
        self.phrase2 = phrase2
        self.level = 0

    def speak(self, phraseNum):

        if phraseNum == 1:
            print(self.phrase1)
        elif phraseNum == 2:
            print(self.phrase2)

    def setLevel(self, newLevel):
        self.level = newLevel
        print (self.name + " is now level " + str(self.level))

Jhin = Character("Jhin", "In carnage, I bloom, like a flower in the dawn.", "My genius will be understood - eventually.")
Vayne = Character("Vayne", "Let us hunt those who have fallen to darkness.", "Evil lurks around every corner.")

Jhin.speak(1)
Jhin.setLevel(2)
Vayne.speak(2)