import tkinter as tk
import random
import time

class MainMenuGUI():
    def __init__(self):
        self.window = tk.Tk()

        self.window.geometry("250x250")
        self.window.title("Yatzy")

        self.buttonFrame = tk.Frame(master=self.window, relief=tk.RIDGE, borderwidth=5)

        self.startGameButton = tk.Button(master=self.buttonFrame, text="Start new game", width=20, height=5)
        self.startGameButton.pack()

        self.loadGameButton = tk.Button(master=self.buttonFrame, text="Load saved game", width=20, height=5)
        self.loadGameButton.pack()

        self.buttonFrame.place(relx=.5, rely=.5, anchor="center")

        self.window.mainloop()

class SavedGamesGUI():
    pass

class GameGUI():
    def __init__(self):
        self.player1State = PlayerGamestate()
        self.player2State = PlayerGamestate()
        self.players = [self.player1State, self.player2State]
        self.Die1 = Die()
        self.Die2 = Die()
        self.Die3 = Die()
        self.Die4 = Die()
        self.Die5 = Die()
        self.dices = [self.Die1, self.Die2, self.Die3, self.Die4, self.Die5]

        self.window = tk.Tk()

        self.window.geometry("500x800")
        self.window.title("Yatzy")

        self.scoreFrame = tk.Frame(master=self.window, background="black")

        self.leftSideLabels = ["YATZY","Ones","Twos","Threes","Fours","Fives","Sixes","Bonus","MidSum","One Pair","Two Pairs","Three of a Kind","Four of a Kind","Small straight","Large straight","Full house","Chance","Yatzy","Score"]
        self.y = 0
        self.x = 0
        for sideLabel in self.leftSideLabels:
            self.createFrame(self.x, self.y, "label", sideLabel)
            self.y += 1

        self.x += 1
        for player in self.players:
            self.y = 0
            self.createFrame(self.x, self.y, "label", "Player")
            self.y += 1

            for score in player.upperSection:
                self.createFrame(self.x, self.y, "button", score)
                self.y += 1

            self.createFrame(self.x, self.y, "label", player.bonus)
            self.y += 1
            self.createFrame(self.x, self.y, "label", player.midSum)
            self.y += 1

            for score in player.lowerSection:
                self.createFrame(self.x, self.y, "button", score)
                self.y += 1

            self.createFrame(self.x, self.y, "label", player.score)
            self.x += 1

        self.scoreFrame.pack()

        self.window.mainloop()


    def createFrame(self,x,y,type,text):
        if type == "button":
            frame = tk.Frame(master=self.scoreFrame,borderwidth=3)
            frame.grid(row=y, column=x, padx=2, pady=2)
            button = tk.Button(master=frame, text=text, width=15)
            button.pack(fill=tk.X)

        if type == "label":
            frame = tk.Frame(master=self.scoreFrame,borderwidth=3)
            frame.grid(row=y, column=x, padx=2, pady=2)
            label = tk.Label(master=frame, text=text, width=15)
            label.pack(fill=tk.X)


        







class PlayerGamestate:
    def __init__(self):
        self.ones = None
        self.twos = None
        self.threes = None
        self.fours = None
        self.fives = None
        self.sixes = None
        self.upperSection = (self.ones, self.twos, self.threes, self.fours, self.fives, self.sixes)
        self.bonus = None
        self.midSum = None
        

        self.onePair = None
        self.twoPairs = None
        self.threeOfAKind = None
        self.fourOfAKind = None
        self.smallStraight = None
        self.largeStraight = None
        self.fullHouse = None
        self.chance = None
        self.yatzy = None
        self.score= None
        self.lowerSection = (self.onePair, self.twoPairs, self.threeOfAKind, self.fourOfAKind, self.smallStraight, self.largeStraight, self.fullHouse, self.chance, self.yatzy)

class Die:
    def __init__(self):
        self.rollDie()


    def rollDie(self):
        self.side = random.randint(1,6)

class Game:
    pass



#test1 = MainMenuGUI()
test2 = GameGUI()