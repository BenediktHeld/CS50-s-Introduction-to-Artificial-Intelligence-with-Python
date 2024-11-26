import random
import turtle
from tkinter import Button, Tk, Label

def pickTheRightNumber(number):
    if number == 1:
        return "red"
    elif number == 2:
        return "blue"
    elif number == 3:
        return "green"
    elif number == 4:
        return "yellow"
    else:
        print("error at color selection")
        return None

def createRandomOrder(colors):
    number = []
    for i in range(len(colors)):
        appended = False
        while not appended:
            numberHelp = random.randint(1, 4)
            if not checkIfContains(numberHelp, number):
                number.append(numberHelp)
                colors[i]["value"] = numberHelp
                colors[i]["color"] = pickTheRightNumber(numberHelp)
                appended = True

def createRandomOrderStart(colors):
    number = []
    for i in range(len(colors)):
        appended = False
        while not appended:
            numberHelp = random.randint(1, 4)
            if not checkIfContains(numberHelp, number):
                number.append(numberHelp)
                colors[i]["rightValue"] = numberHelp
                appended = True

def checkIfContains(number, lst):
    return number in lst

def CheckIfRight(colors):
    ret = True
    for i in range(len(colors)):
        if colors[i]["value"] != colors[i]["rightValue"]:
            ret = False
            break
    return ret

def DisplayGame(colors, round_number):
    global screen
    screen = turtle.Screen()
    screen.setup(width=600, height=400)
    screen.title(f"Mastermind - Runde {round_number}")
    screen.bgcolor("lightgray")

    XStartCord = -50 * len(colors)
    for i in range(len(colors)):
        t1 = turtle.Turtle()
        t1.shape("circle")
        t1.shapesize(stretch_wid=2, stretch_len=2, outline=1)
        t1.penup()
        t1.goto(XStartCord, 0)
        XStartCord += 70
        t1.color(colors[i]["color"])

def DisplayBoard():
    global root, correctness_label, round_label
    # TKinter-Fenster für Buttons und Informationen erstellen
    root = Tk()
    root.title("Mastermind Steuerung")

    # Labels für aktuelle Runde und Anzahl Richtiger
    round_label = Label(root, text=f"Runde: {round_number}", font=('Helvetica', 14))
    round_label.pack(padx=10, pady=5)

    correctness_label = Label(root, text=f"Anzahl Richtiger: {CheckValueOfRight(colors)}", font=('Helvetica', 14))
    correctness_label.pack(padx=10, pady=5)

    # Buttons erstellen und Funktionen zuweisen
    RightButton = Button(root, text="Richtig", command=right_button_action)
    WrongButton = Button(root, text="Falsch", command=wrong_button_action)

    # Buttons im Fenster anordnen
    RightButton.pack(side="left", padx=10, pady=5)
    WrongButton.pack(side="left", padx=10, pady=5)

def right_button_action():
    if CheckIfRight(colors):
        next_round()
    else:
        correctness_label.config(text=f"Anzahl Richtiger: {CheckValueOfRight(colors)}")
        print("Fehlende Übereinstimmung")

def wrong_button_action():
    createRandomOrder(colors)
    DisplayGame(colors, round_number)
    correctness_label.config(text=f"Anzahl Richtiger: {CheckValueOfRight(colors)}")

def next_round():
    global round_number
    screen.bye()  # Schließt das Turtle-Fenster
    root.destroy()  # Schließt das Tkinter-Fenster
    round_number += 1
    run_game()  # Startet die nächste Runde

def CheckValueOfRight(colors):
    count = 0
    for i in range(len(colors)):
        if colors[i]["value"] == colors[i]["rightValue"]:
            count += 1
    return count

def run_game():
    global colors, round_number

    colors = [{"color": "red", "value": 1, "rightValue": 1},
              {"color": "blue", "value": 2, "rightValue": 2},
              {"color": "green", "value": 3, "rightValue": 3},
              {"color": "yellow", "value": 4, "rightValue": 4}]

    # Setze den geheimen Code zu Beginn des Spiels
    createRandomOrderStart(colors)

    # Hauptspielanzeige
    createRandomOrder(colors)
    DisplayGame(colors, round_number)
    DisplayBoard()
    root.mainloop()

# Initialisierung der ersten Runde
round_number = 1
run_game()