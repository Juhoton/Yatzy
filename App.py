import tkinter as tk
import random

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

class PlayerGamestate:
    def __init__(self):
        self.ones = None
        self.twos = None
        self.threes = None
        self.fours = None
        self.fives = None
        self.sixes = None
        self.upperSection = (self.ones, self.twos, self.threes, self.fours, self.fives, self.sixes)

        self.onePair = None
        self.twoPairs = None
        self.threeOfAKind = None
        self.fourOfAKind = None
        self.smallStraight = None
        self.largeStraight = None
        self.fullHouse = None
        self.chance = None
        self.yatzy = None
        self.lowerSection = (self.onePair, self.twoPairs, self.threeOfAKind, self.fourOfAKind, self.smallStraight, self.largeStraight, self.fullHouse, self.chance, self.yatzy)

class Die:
    def __init__(self):
        self.rollDie()


    def rollDie():
        side = random.randint(1,6)







