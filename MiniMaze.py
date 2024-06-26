
from random import random
import os

#basic board layout 9 by 10
control1=[['|','-','-','-','-','-','-','-','|',],
    ['|',' ',' ',' ',' ',' ',' ',' ','|',],
    ['|',' ',' ',' ',' ',' ',' ',' ','|',],
    ['|',' ',' ',' ',' ',' ',' ',' ','|',],
    ['|',' ',' ',' ',' ',' ',' ',' ','|',],
    ['|',' ',' ',' ',' ',' ',' ',' ','|',],
    ['|',' ',' ',' ',' ',' ',' ',' ','|',],
    ['|',' ',' ',' ',' ',' ',' ',' ','|',],
    ['|',' ',' ',' ',' ',' ',' ',' ','|',],
    ['|','-','-','-','-','-','-','-','|',]]

#basic board layout 21 by 21
control2=[['|','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','|'],#0
          ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'],
          ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'],
          ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'],
          ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'],
          ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'],#5
          ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'],
          ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'],
          ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'],
          ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'],
          ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'],#10
          ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'],
          ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'],
          ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'],
          ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'],
          ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'],#15
          ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'],
          ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'],
          ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'],
          ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'],
          ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'],#20
          ['|','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','|']]

#boards :

l1=[['|','-','-','-','-','-','-','-','|',],
    ['|','●',' ',' ',' ','■',' ',' ','|',],
    ['|','■','■','■',' ','■',' ','■','|',],
    ['|',' ',' ',' ',' ','■',' ',' ','|',],
    ['|','■','■',' ','■','■','■',' ','|',],
    ['|',' ','■',' ','■',' ',' ',' ','|',],
    ['|',' ',' ',' ',' ',' ','■','■','|',],
    ['|',' ','■',' ','■','■','■',' ','|',],
    ['|',' ','■',' ',' ',' ',' ',' ','|',],
    ['|','-','-','-','-','-','-','-','|',]]

l2=[['|','-','-','-','-','-','-','-','|',],
    ['|',' ','■','■','■',' ',' ',' ','|',],
    ['|',' ',' ','■',' ',' ','■',' ','|',],
    ['|',' ','■','■',' ','■','■',' ','|',],
    ['|',' ',' ',' ','■',' ',' ',' ','|',],
    ['|',' ','■',' ',' ','■','■',' ','|',],
    ['|',' ',' ','■',' ',' ',' ',' ','|',],
    ['|','■',' ','■',' ','■','■','■','|',],
    ['|','●',' ','■',' ',' ',' ','■','|',],
    ['|','-','-','-','-','-','-','-','|',]]

l3=[['|','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','|'],#0
    ['|',' ','■',' ',' ',' ','■',' ','■',' ','■',' ','■',' ',' ',' ','■',' ',' ',' ','■','|'],
    ['|',' ','■',' ','■',' ','■',' ',' ',' ','■',' ',' ',' ','■',' ','■',' ','■',' ',' ','|'],
    ['|',' ','■',' ','■',' ','■','■','■',' ',' ','■',' ',' ','■',' ',' ',' ','■',' ','■','|'],
    ['|',' ',' ',' ',' ',' ',' ',' ',' ','■',' ',' ','■','■',' ',' ','■','■','■',' ','■','|'],
    ['|','■',' ','■','■','■','■','■',' ',' ','■',' ',' ',' ','■',' ','■',' ',' ',' ',' ','|'],#5
    ['|',' ',' ',' ',' ',' ',' ',' ','■',' ','■','■','■',' ','■',' ','■',' ','■',' ','■','|'],
    ['|',' ','■',' ','■',' ','■',' ','■','■',' ',' ',' ',' ','■',' ',' ',' ',' ',' ',' ','|'],
    ['|',' ','■',' ','■',' ','■','■',' ',' ','■',' ','■','■','■','■','■',' ','■',' ','■','|'],
    ['|','■',' ',' ','■',' ',' ',' ','■',' ','■',' ','■','◯',' ',' ',' ',' ','■',' ',' ','|'],
    ['|',' ',' ','■','■',' ','■','●','■',' ','■',' ','■','■','■',' ','■',' ','■',' ','■','|'],#10
    ['|','■','■',' ',' ',' ','■',' ',' ',' ',' ',' ','■',' ',' ','■',' ',' ','■',' ','■','|'],
    ['|','■',' ','■','■','■','■',' ','■',' ','■','■','■','■',' ','■','■','■','■',' ',' ','|'],
    ['|',' ',' ',' ','■',' ',' ',' ',' ',' ',' ','■',' ',' ',' ','■',' ',' ',' ',' ',' ','|'],
    ['|',' ','■',' ',' ',' ','■',' ','■','■',' ','■','■',' ','■',' ',' ','■','■','■',' ','|'],
    ['|',' ',' ','■',' ','■','■',' ',' ','■',' ',' ','■',' ','■',' ','■',' ',' ',' ',' ','|'],#15
    ['|',' ','■','■',' ',' ',' ','■','■','■',' ',' ','■',' ',' ',' ','■',' ','■','■','■','|'],
    ['|',' ','■',' ','■','■','■',' ',' ',' ','■','■',' ',' ','■',' ','■',' ',' ',' ',' ','|'],
    ['|',' ','■',' ',' ',' ','■',' ','■',' ',' ',' ','■',' ','■',' ','■','■','■',' ','■','|'],
    ['|',' ',' ',' ','■',' ',' ',' ',' ','■','■',' ',' ',' ','■',' ',' ',' ',' ',' ',' ','|'],#20
    ['|','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','|']]


def board () :
    # board printing, por small boards the size is lenght(10) by lenght-1(9), else size is lenght by lenght
    # in flashlight mode only the positions near the player are diplayed, else a space is printed
    print("")
    if g==2 :
        if n==1 or n==2 :
            for i in range(len(b)) :
                for j in range (len(b)-1) :
                    if pi-1==i and pj-1==j : print(b[i][j]," ",end="")
                    if pi==i and pj-1==j : print(b[i][j]," ",end="")
                    if pi+1==i and pj-1==j : print(b[i][j]," ",end="")
                    if pi-1==i and pj==j : print(b[i][j]," ",end="")
                    if pi==i and pj==j : print(b[i][j]," ",end="")
                    if pi+1==i and pj==j : print(b[i][j]," ",end="")
                    if pi-1==i and pj+1==j : print(b[i][j]," ",end="")
                    if pi==i and pj+1==j : print(b[i][j]," ",end="")
                    if pi+1==i and pj+1==j : print(b[i][j]," ",end="")
                    else : print ('  ',end="")
                print()
        else :
            for i in range(len(b)) :
                for j in range (len(b)) :
                    if pi-1==i and pj-1==j : print(b[i][j]," ",end="")
                    if pi==i and pj-1==j : print(b[i][j]," ",end="")
                    if pi+1==i and pj-1==j : print(b[i][j]," ",end="")
                    if pi-1==i and pj==j : print(b[i][j]," ",end="")
                    if pi==i and pj==j : print(b[i][j]," ",end="")
                    if pi+1==i and pj==j : print(b[i][j]," ",end="")
                    if pi-1==i and pj+1==j : print(b[i][j]," ",end="")
                    if pi==i and pj+1==j : print(b[i][j]," ",end="")
                    if pi+1==i and pj+1==j : print(b[i][j]," ",end="")
                    else : print ('  ',end="")
                print()
    if g==1 :
        if n==1 or n==2 :
            for i in range(len(b)) :
                for j in range (len(b)-1) :
                    print(b[i][j]," ",end="")
                print()
        else :
            for i in range(len(b)) :
                for j in range (len(b)+1) :
                    print(b[i][j]," ",end="")
                print()

def move () :
    # screen is cleared, while the move is invalid player introduces move
    # when a valid move is introduced player is moved
    os.system('cls')
    global pi
    global pj
    board()
    c=1
    while c==1 :
        m=input("make move : ")
        if m=='w':
            if b[pi-1][pj]==" " or b[pi-1][pj]=="◯" :
                c=0
                b[pi][pj]=" "
                pi-=1
                b[pi][pj]='●'
            else : print("invalid move")
        if m=='a':
            if b[pi][pj-1]==" " or b[pi][pj-1]=="◯" :
                c=0  
                b[pi][pj]=" "
                pj-=1
                b[pi][pj]='●'
            else : print("invalid move") 
        if m=='s':
            if b[pi+1][pj]==" " or b[pi+1][pj]=="◯" :
                c=0  
                b[pi][pj]=" "
                pi+=1
                b[pi][pj]='●'
            else : print("invalid move")
        if m=='d':
            if b[pi][pj+1]==" " or b[pi][pj+1]=="◯" :
                c=0  
                b[pi][pj]=" "
                pj+=1
                b[pi][pj]='●'
            else : print("invalid move")
    #print(pi,pj)       

# gamemode and board selection      
g=int(input("gamemode : 1.normal , 2.flashlight "))
n=int(input("chose board : 1-3; 9-random board "))

# chosen board is copied in play board, player and win positions are initialized
if n==9 :
    n=random()*10%3
if n==1 : 
    b=l1
    pi=1
    pj=1
    b[pi][pj]='●'
    wi=8
    wj=7
    b[wi][wj]='◯'
if n==2 :
    b=l2
    pi=8
    pj=1
    b[pi][pj]='●'
    wi=4
    wj=5
    b[wi][wj]='◯'
if n==3 :
    b=l3
    pi=10
    pj=7
    b[pi][pj]='●'
    wi=9
    wj=13
    b[wi][wj]='◯'

# game rules
print('●  player, use w a s d to move')
print('■  wall, no you cant pass thru it')
print('|,- exterior wall, you are at the edge of the maze')
print('◯  maze exit, yipeeeee')

# while not in win pos, player moves
while(pi!=wi or pj!=wj) :
    move()

# endgame, winplace becomes star, clear screen, win announcement
b[wi][wj]="✪"
os.system('cls')
board()
print("level completed !")
print("game concluded")
n=input()
