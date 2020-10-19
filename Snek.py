from tkinter import *
import time
import random

#variables
gameW = 800
gameH = 600

dotSize = 10
totalDots = (gameW *gameH )/(dotSize*dotSize)
loopDelay = 100

#list of colors
#https://www.tcl.tk/man/tcl/TkCmd/colors.htm
bgColor = "black"
snekColor = "green"
snekBorderColor = "yellow"
appleColor = "red"
appleBorderColor = "white"
dots = 3

#snake direction
leftDirection = False
rightDirection = True
upDirection = False
downDirection = False

#random apple place


applePoint = (random.randint(2, gameW/dotSize-2) * 10, random.randint(2, gameH/dotSize-2) * 10)
print(applePoint)
segments = []

#add snake segments
for i in range(0, dots):
    segments.append((150 - i * dotSize, 150))


def onKeyPressed(e):
    # not sure why I need global here
    global rightDirection
    global leftDirection
    global upDirection
    global downDirection

    key = e.keysym
    if key == "Right" and not rightDirection:
        leftDirection = False
        rightDirection = True
        upDirection = False
        downDirection = False

    if key == "Left" and not leftDirection:
        leftDirection = True
        rightDirection = False
        upDirection = False
        downDirection = False

    if key == "Up" and not upDirection:
        leftDirection = False
        rightDirection = False
        upDirection = True
        downDirection = False

    if key == "Down" and not downDirection:
        leftDirection = False
        rightDirection = False
        upDirection = False
        downDirection = True

def checkApple():
    global dots
    global applePoint

    #snakes head == apple
    print(segments[0])
    print(applePoint)
    if segments[0][0] == applePoint[0] and segments[0][1] == applePoint[1]:
        for i in range(1):
            segments.append((0,0))
            dots = dots+1
        applePoint = (random.randint(2, gameW / dotSize-2) * 10, random.randint(2, gameH / dotSize-2) * 10)
        print("apple collision")

def checkCollision():
    #return true or false if we hit something
    #x component of head of snake
    if segments[0][0] < 0 or segments[0][0] > gameW:
        return True

    if segments[0][1] < 0 or segments[0][1] > gameH:
        return True

    #see if we bite ourselves
    for i in range(dots-1, 1, -1):
        if segments[i][0] == segments[0][0] and segments[i][1] == segments[0][1]:
            return True

    return False


def gameLoop():
    #draw background
    snekCanvas.delete(ALL)
    snekCanvas.create_rectangle(0,0,gameW, gameH, fill = bgColor )

    #draw apple
    snekCanvas.create_oval(applePoint[0], applePoint[1], applePoint[0] + dotSize , applePoint[1] + dotSize,
                                fill=appleColor, outline = appleBorderColor)
    # draw snake
    snekCanvas.create_oval(segments[0][0], segments[0][1], segments[0][0] + dotSize, segments[0][1] + dotSize,
                                fill="blue", outline="white")
    for i in range(1,dots):
        snekCanvas.create_rectangle(segments[i][0], segments[i][1], segments[i][0] + dotSize, segments[i][1] + dotSize,
                                fill=snekColor, outline=snekBorderColor)

    #the body
    for i in range(dots - 1, 0, -1):
        segments[i] = (segments[(i - 1)][0], segments[(i - 1)][1])

    #the head
    if leftDirection:
        segments[0] = (segments[0][0] - dotSize, segments[0][1])

    if rightDirection:
        segments[0] = (segments[0][0] + dotSize, segments[0][1])

    if upDirection:
        segments[0] = (segments[0][0] , segments[0][1] - dotSize)

    if downDirection:
        segments[0] = (segments[0][0] , segments[0][1] + dotSize)

    checkApple()
    gameOver = checkCollision()

    if not gameOver:
        listenID = root.after(loopDelay, gameLoop)
    else:
        print("Game over")
        snekCanvas.create_text(gameW/2,gameH/2,fill="white",font="Times 40 bold",
                        text="GAME OVER")
        snekCanvas.create_text(gameW / 2+2, gameH / 2+2, fill="yellow", font="Times 40 bold",
                               text="GAME OVER")


root = Tk()
root.title("Snek Game")
root.configure(background='sky blue')

frame1 = Frame(root, bg="sky blue", bd=10)

frame1.pack(side=TOP)

snekCanvas = Canvas(frame1, width=gameW, height=gameH)
snekCanvas.bind_all("<Key>", onKeyPressed)
snekCanvas.pack()

#start the loop
listenID = root.after(loopDelay, gameLoop)
mainloop()