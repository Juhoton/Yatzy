import tkinter as tk
import random
from collections import Counter
import pickle
import os
class MainMenu():
    def __init__(self, window):
        self.createMainMenu()

    def createMainMenu(self):
        window.geometry("250x250")
        window.title("Yatzy")

        self.buttonFrame = tk.Frame(master=window, relief=tk.RIDGE, borderwidth=5)

        self.startGameButton = tk.Button(master=self.buttonFrame, text="Start new game", width=20, height=5, command=self.startGame)
        self.startGameButton.pack()

        self.loadGameButton = tk.Button(master=self.buttonFrame, text="Load saved game", width=20, height=5, command=self.loadGame)
        self.loadGameButton.pack()

        self.buttonFrame.place(relx=.5, rely=.5, anchor="center")
        
    def startGame(self):
        self.buttonFrame.destroy()
        Game(window)

    def loadGame(self):
        self.buttonFrame.destroy()
        directory = "savedGames"
        window.geometry("500x500")
        window.title("Yatzy")

        self.buttonFrame = tk.Frame(master=window, relief=tk.RIDGE, borderwidth=5)

        for fileName in os.listdir(directory):
            self.startGameButton = tk.Button(master=self.buttonFrame, text=fileName, width=20, height=5, command=lambda fileName = fileName:self.startSavedGame(fileName))
            self.startGameButton.pack()


        self.buttonFrame.place(relx=.5, rely=.5, anchor="center")
        
    def startSavedGame(self, filename):
        with open ("savedGames/"+filename, "rb") as f:
            tempTuple = pickle.load(f)
        Game(window, tempTuple)


class SavedGames():
    pass

class Game():

    def __init__(self, *args):
        window.geometry("600x900")
        window.title("Yatzy")
        self.gameFrame = tk.Frame(master=window)
        self.dice1 = tk.PhotoImage(file='Dices\dice1.png')
        self.dice2 = tk.PhotoImage(file='Dices\dice2.png')
        self.dice3 = tk.PhotoImage(file='Dices\dice3.png')
        self.dice4 = tk.PhotoImage(file='Dices\dice4.png')
        self.dice5 = tk.PhotoImage(file='Dices\dice5.png')
        self.dice6 = tk.PhotoImage(file='Dices\dice6.png')

        if len(args) == 1:
            self.player1State = PlayerGamestate()
            self.player2State = PlayerGamestate()
            self.playerTurn = 1
            self.rollsLeft = 3
            self.players = [self.player1State, self.player2State]
            self.Die1 = Die()
            self.Die2 = Die()
            self.Die3 = Die()
            self.Die4 = Die()
            self.Die5 = Die()
            self.dices = [self.Die1, self.Die2, self.Die3, self.Die4, self.Die5]
        else:
            self.players = args[1][0]
            self.playerTurn = args[1][1]
            self.rollsLeft = args[1][2]
            self.Die1 = Die(args[1][3][0])
            self.Die2 = Die(args[1][3][1])
            self.Die3 = Die(args[1][3][2])
            self.Die4 = Die(args[1][3][3])
            self.Die5 = Die(args[1][3][4])
            self.dices = [self.Die1, self.Die2, self.Die3, self.Die4, self.Die5]

        self.createScoreGrid()
        self.createDices()
        self.gameFrame.place(relx=.5, rely=.5, anchor="center")
        window.bind('<Escape>',lambda e: self.pauseMenu(e))

    def reCreateAll(self):
        self.scoreFrame.destroy()
        self.diceCheckButtons.destroy()
        self.createScoreGrid()
        self.createDices()

    def createScoreGrid(self):
        self.scoreFrame = tk.Frame(master=self.gameFrame, background="black")
        self.scoreButtons = []
        y = 0
        x = 0
        for sideLabel in ["YATZY","Ones","Twos","Threes","Fours","Fives","Sixes","Bonus","MidSum","One Pair","Two Pairs","Three of a Kind","Four of a Kind","Small straight","Large straight","Full house","Chance","Yatzy","Score"]:
            self.createFrame(x, y, sideLabel,self.players[0])
            y += 1

        x += 1
        for player in self.players:
            y = 0
            self.createFrame(x, y, "Player",player)
            y += 1
            for score in player.getUpperSection():
                self.createFrame(x, y, score,player)
                y += 1

            self.createFrame(x, y, player.getBonus(),player)
            y += 1
            self.createFrame(x, y, player.getMidSum(),player)
            y += 1
            for score in player.getLowerSection():
                self.createFrame(x, y, score,player)
                y += 1

            self.createFrame(x, y, player.getScore(),player)
            x += 1

        self.scoreFrame.pack()

    def createFrame(self,x,y,text,player):
        if self.players.index(player) != (self.playerTurn-1) or self.rollsLeft == 3:
            frame = tk.Frame(master=self.scoreFrame,borderwidth=3)
            frame.grid(row=y, column=x, padx=2, pady=2)
            label = tk.Label(master=frame, text=text, width=15)
            label.pack(fill=tk.X)
        elif text == None:
            frame = tk.Frame(master=self.scoreFrame,borderwidth=3)
            frame.grid(row=y, column=x, padx=2, pady=2)
            button = tk.Button(master=frame, text="", width=15, command=lambda y=y: self.setScore(y))
            button.pack(fill=tk.X)
            self.scoreButtons.append((x,y,button))
        else:
            frame = tk.Frame(master=self.scoreFrame,borderwidth=3)
            frame.grid(row=y, column=x, padx=2, pady=2)
            label = tk.Label(master=frame, text=text, width=15)
            label.pack(fill=tk.X)

    def createDices(self):
        self.diceCheckButtons = tk.Frame(master=self.gameFrame)
        y = 0
        x = 0
        for die in self.dices:
            self.createDie(x, y, die)
            x += 1

        self.createRollButton()
        self.diceCheckButtons.pack(side=tk.TOP)
        return self.diceCheckButtons

    def createDie(self, x, y, die):
        self.frame = tk.Frame(master=self.diceCheckButtons)
        self.frame.grid(row=y, column=x, padx=2, pady=2)
        self.label = tk.Label(master=self.frame, image=self.getDieImage(die))
        self.label.pack()
        self.checkButton = tk.Checkbutton(master=self.frame, variable= die.selected, onvalue=True, offvalue=False) # 
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

    def createRollButton(self):
        if self.rollsLeft != 0:
            frame = tk.Frame(master=self.diceCheckButtons,borderwidth=3)
            frame.grid(row=1, column=2)
            button = tk.Button(master=frame, text="Roll", width=15, command=self.rollDices)
            button.pack(fill=tk.X)
        
    def rollDices(self):
        self.rollsLeft -= 1
        if self.rollsLeft == 2:
            for die in self.dices:
                die.rollDie()
            self.reCreateAll()
        else:
            for die in self.dices:
                if die.selected.get() == False:
                    die.rollDie()
            self.diceCheckButtons.destroy()
            self.createDices()
        self.checkPossibleScores()

    def checkPossibleScores(self):
        for scoreButton in self.scoreButtons:
            scoreButton[2].config(text=PlayerGamestate.checkDiceValue(scoreButton[1],self.dices))

    def setScore(self,y):
        self.players[self.playerTurn-1].setScore(y,PlayerGamestate.checkDiceValue(y,self.dices))
        self.playerTurn +=1
        if self.playerTurn > len(self.players):
            self.playerTurn = 1
        self.rollsLeft = 3
        self.reCreateAll()
    
    def pauseMenu(self,e):
        self.scoreFrame.destroy()
        self.diceCheckButtons.destroy()
        self.buttonFrame = tk.Frame(master=self.gameFrame, relief=tk.RIDGE, borderwidth=5)

        self.startGameButton = tk.Button(master=self.buttonFrame, text="back", width=20, height=5, command=self.back)
        self.startGameButton.pack()

        self.loadGameButton = tk.Button(master=self.buttonFrame, text="Save game", width=20, height=5, command=self.saveGame)
        self.loadGameButton.pack()

        self.saveName = ""
        self.saveEntry = tk.Entry(master=self.buttonFrame, textvariable=self.saveName)
        self.saveEntry.pack()

        self.mainMenuButton = tk.Button(master=self.buttonFrame, text="Main menu", width=20, height=5, command=self.toMainMenu)
        self.mainMenuButton.pack()

        self.buttonFrame.place(relx=.5, rely=.5, anchor="center")

    def back(self):
        self.buttonFrame.destroy()
        self.createScoreGrid()
        self.createDices()
        self.checkPossibleScores()

    def saveGame(self):
        tempDices = []
        for die in self.dices:
            tempDices.append(die.getData())
        tempTuple = (self.players, self.playerTurn, self.rollsLeft, tempDices)
        with open("savedGames/" + self.saveEntry.get(), "wb") as f:
            pickle.dump(tempTuple, f, protocol=pickle.HIGHEST_PROTOCOL)
    
    def toMainMenu(self):
        self.buttonFrame.destroy()
        MainMenu(window)

class PlayerGamestate:
    def __init__(self):
        self.ones = None
        self.twos = None
        self.threes = None
        self.fours = None
        self.fives = None
        self.sixes = None
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
        self.__score= 0

    def getUpperSection(self):
        return (self.ones, self.twos, self.threes, self.fours, self.fives, self.sixes)

    def getLowerSection(self):
        return (self.onePair, self.twoPairs, self.threeOfAKind, self.fourOfAKind, self.smallStraight, self.largeStraight, self.fullHouse, self.chance, self.yatzy)

    def getBonus(self):
        self.checkBonus()
        return self.__bonus

    def getMidSum(self):
        self.checkMidSum()
        return self.__midSum

    def getScore(self):
        self.checkScore()
        return self.__score
    def checkBonus(self):
        sum = 0
        for value in self.getUpperSection():
            if value != None:
                sum += value
        
        if sum >= 63:
            self.__bonus = 50

    def checkMidSum(self):
        self.__midSum = 0
        for value in self.getUpperSection():
            if value != None:
                self.__midSum += value

    def checkScore(self):
        self.__score = self.getMidSum()
        for value in self.getLowerSection():
            if value != None:
                self.__score += value
        return self.__score

    def setScore(self,y,score):
        match y:
            case 1:
                self.ones = score
            case 2:
                self.twos = score
            case 3:
                self.threes = score
            case 4:
                self.fours = score
            case 5:
                self.fives = score
            case 6:
                self.sixes = score
            case 9:
                self.onePair = score
            case 10:
                self.twoPairs = score
            case 11:
                self.threeOfAKind = score
            case 12:
                self.fourOfAKind = score
            case 13:
                self.smallStraight = score
            case 14:
                self.largeStraight = score
            case 15:
                self.fullHouse = score
            case 16:
                self.chance = score
            case 17:
                self.yatzy = score
                

    @staticmethod
    def checkDiceValue(y, dices):
        tempList=[]
        for die in dices:
            tempList.append(die.side)
        sideCount = Counter(tempList)
        value = 0
        match y:
            case 1: #Ones
                for die in dices:
                    if die.side == 1:
                        value += 1
            case 2: #Twos
                for die in dices:
                    if die.side == 2:
                        value += 2
            case 3: #Threes
                for die in dices:
                    if die.side == 3:
                        value += 3
            case 4: #Fours
                for die in dices:
                    if die.side == 4:
                        value += 4
            case 5: #Fives
                for die in dices:
                    if die.side == 5:
                        value += 5
            case 6: #Sixes
                for die in dices:
                    if die.side == 6:
                        value += 6
            case 9: #One Pair
                for side in sideCount:
                    if sideCount[side] >= 2 and side * 2 > value:
                        value = side * 2
            case 10: #Two Pairs
                pairCount=0
                for side in sideCount:
                    if sideCount[side] >= 2:
                        pairCount+=1
                        value += side*2
                if pairCount != 2:
                        value = 0
            case 11: # Three of a Kind
                for side in sideCount:
                    if sideCount[side] >= 3:
                        value += side*3
            case 12: #Four of a Kind
                for side in sideCount:
                    if sideCount[side] >= 4:
                        value += side*4
            case 13: #Small Straight
                value = 15
                for side in sideCount:
                    if sideCount[side] != 1 or side == 6:
                        value = 0
            case 14: #Large Straight
                value = 20
                for side in sideCount:
                    if sideCount[side] != 1 or side == 1:
                        value = 0
            case 15: #Full House
                pair = 0
                for side in sideCount:
                    if sideCount[side] == 3:
                        for side2 in sideCount:
                            if sideCount[side2] == 2:
                                value = side*3 + side2*2
            case 16: #Chance
                for die in dices:
                    value += die.side
            case 17: #Yatzy
                for side in sideCount:
                    if sideCount[side] == 5:
                        value = 50

        return value

class Die:
    def __init__(self, *args):
        if len(args) == 0:
            self.rollDie()
            self.selected = tk.BooleanVar()
        else:
            self.side = args[0][0]
            self.selected = tk.BooleanVar()

    def rollDie(self):
        self.side = random.randint(1,6)
    
    def setSelected(self,state):
        self.selected = state

    def getData(self):
        return (self.side, self.selected.get())


window = tk.Tk()

MainMenu(window)

window.mainloop()