import tkinter as tk
import random
from tkinter import ttk
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
        self.window.geometry("600x1000")
        self.window.title("Yatzy")
        self.dice1 = tk.PhotoImage(file='Dices\dice1.png')
        self.dice2 = tk.PhotoImage(file='Dices\dice2.png')
        self.dice3 = tk.PhotoImage(file='Dices\dice3.png')
        self.dice4 = tk.PhotoImage(file='Dices\dice4.png')
        self.dice5 = tk.PhotoImage(file='Dices\dice5.png')
        self.dice6 = tk.PhotoImage(file='Dices\dice6.png')

        self.createScoreGrid()
        self.createDiceCheckButtons()

        self.window.mainloop()

    def createScoreGrid(self):
        self.scoreFrame = tk.Frame(master=self.window, background="black")
        y = 0
        x = 0
        for sideLabel in ["YATZY","Ones","Twos","Threes","Fours","Fives","Sixes","Bonus","MidSum","One Pair","Two Pairs","Three of a Kind","Four of a Kind","Small straight","Large straight","Full house","Chance","Yatzy","Score"]:
            self.createFrame(x, y, sideLabel)
            y += 1

        x += 1
        for player in self.players:
            y = 0
            self.createFrame(x, y, "Player")
            y += 1
            for score in player.upperSection:
                self.createFrame(x, y, score)
                y += 1

            self.createFrame(x, y, player.getBonus())
            y += 1
            self.createFrame(x, y, player.getMidSum())
            y += 1
            for score in player.lowerSection:
                self.createFrame(x, y, score)
                y += 1

            self.createFrame(x, y, player.score)
            x += 1

        self.scoreFrame.pack()

    def createFrame(self,x,y,text):
        if text == None:
            frame = tk.Frame(master=self.scoreFrame,borderwidth=3)
            frame.grid(row=y, column=x, padx=2, pady=2)
            button = tk.Button(master=frame, text=text, width=15)
            button.pack(fill=tk.X)
        else:
            frame = tk.Frame(master=self.scoreFrame,borderwidth=3)
            frame.grid(row=y, column=x, padx=2, pady=2)
            label = tk.Label(master=frame, text=text, width=15)
            label.pack(fill=tk.X)

    def createDiceCheckButtons(self):
        self.diceCheckButtons = tk.Frame(master=self.window)
        y = 0
        x = 0
        for die in self.dices:
            self.createCheckButton(x, y, die)
            x += 1

        self.diceCheckButtons.pack(side=tk.TOP)

    def createCheckButton(self, x, y, die):
        self.frame = tk.Frame(master=self.diceCheckButtons)
        self.frame.grid(row=y, column=x, padx=2, pady=2)
        self.label = tk.Label(master=self.frame, image=self.getDieImage(die))
        self.label.pack()
        self.on = tk.BooleanVar()
        self.checkButton = tk.Checkbutton(master=self.frame, variable=self.on, onvalue=True, offvalue=False) # 
        self.checkButton.pack()

    def getDieImage(self, die):
        if die.side == 1:
            return self.dice1
        if die.side == 2:
            return self.dice2
        if die.side == 3:
            return self.dice3
        if die.side == 4:
            return self.dice4
        if die.side == 5:
            return self.dice5
        if die.side == 6:
            return self.dice6


class PlayerGamestate:
    def __init__(self):
        self.ones = None
        self.twos = None
        self.threes = None
        self.fours = None
        self.fives = None
        self.sixes = None
        self.upperSection = (self.ones, self.twos, self.threes, self.fours, self.fives, self.sixes)
        self.__bonus = 0
        self.__midSum = 0
        

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

    def getBonus(self):
        self.checkBonus()
        return self.__bonus

    def getMidSum(self):
        self.checkMidSum()
        return self.__midSum

    def checkBonus(self):
        sum = 0
        for value in self.upperSection:
            if value != None:
                sum += value
        
        if sum >= 63:
            self.__bonus = 50

    def checkMidSum(self):
        self.__midSum = 0
        for value in self.upperSection:
            if value != None:
                self.__midSum += value

class Die:
    def __init__(self):
        self.rollDie()

    def rollDie(self):
        self.side = random.randint(1,6)

class Game:
    pass



#test1 = MainMenuGUI()
test2 = GameGUI()