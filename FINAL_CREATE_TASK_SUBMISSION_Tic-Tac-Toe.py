import pygame
import random
import time
from pygame.locals import *
from tkinter import *
from tkinter import messagebox
pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (235,255,0)
pink = (175,0,175)
bright_red = (255,48,48)
grey = (100,100,100)
x = 0
y = 0

nums_list = ["","","","","","","","",""]

turn = 0
mouse_x = 0
mouse_y = 0

Tk().wm_withdraw()
messagebox.showinfo('TIC-TAC-TOE Game','How to Play:\n- There is a grid of 9 boxes\n- There are two teams;"X" and "O"\n- "O" is first, followed by "X". they keep alternating.\n- The end goal is to make a straight line of your shape(it dosent matter which way) and to prevent your opponent from doing the same.\n Good Luck! :)')

def find_winner(board, a, b, c):
  if board[a] == board[b] == board[c]:
    if board[a] == "":
      return None
    else:
      return board[a]


winner_lines = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]


# Checks if someone won.
def check_for_completion(board, turn):
  # 5 turns must be taken for there to be a winner.
  if turn < 5:
    return None

  for t in winner_lines:
    if find_winner(board, t[0], t[1], t[2]) != None:
      if (board[t[0]] == 'x'):
        print("Game Over! The winner is player X!")
        show_text("Game Over! The winner is player X!",10,10,black)
      else:
        print("Game Over! The winner is player O!")
        show_text("Game Over! The winner is player O!",10,10,black)
      pygame.display.update()
      time.sleep(5)
      return board[t[0]]

  # If 9 turns are taken and there is no winner.
  # declare a draw.
  if turn == 9:
    print("Game Over! Its a Draw!")
    show_text("Game Over! Its a Draw!",10,10,black)
    pygame.display.update()
    time.sleep(5)
  
  return None

def draw_x(x,y):
    pygame.draw.line(screen,green,(x,y),(x+200,y+200),2)
    pygame.draw.line(screen,green,(x+200,y),(x,y+200),2)

def draw_o(x,y):
    pygame.draw.circle(screen,green,(x,y),55)

def show_text(msg,x,y,color):
    fontobj =  pygame.font.SysFont('freesans',32)
    msgobj  =  fontobj.render(msg,False,color)
    screen.blit(msgobj,(x,y))

screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Tic Tac Toe!!")
y = 0
x = 0
for i in nums_list:
  pygame.draw.rect(screen,red,(x,y,200,200))
  red,blue=blue,red
  x = x + 200
  if x == 600:
    x = x - 600
    y = y + 200

def take_turn(index, x1, x2, y1, y2):
  if mouse_x>x1 and mouse_x<x2 and mouse_y>y1 and mouse_y<y2:
    if nums_list[index] != "":
      # Checks to see if an occupied square has been clicked on.
      return False

    if turn%2 == 1:
        draw_x(x1, y1)
        nums_list[index] = "x"
    else:
        draw_o(x1+100, y1+100)
        nums_list[index] = "o"

  return True

while True:
    pygame.display.update()

    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        exit()
      if event.type == MOUSEBUTTONDOWN and event.button==1:
        mouse_x = event.pos[0]
        mouse_y = event.pos[1]

        index = 0
        errorfound = False

        for y_var in range(0, 600, 200):
          for x_var in range(0, 600, 200):
            if (take_turn(index, x_var, x_var+200, y_var, y_var+200) == False):
              errorfound = True
              break
            index += 1
        
        if errorfound == True:
          # Someone clicked in an occupied
          # square. We should ignore this.
          continue

        turn = turn+1
        print(nums_list)
        if (check_for_completion(nums_list, turn) != None) or (turn == 9):
          pygame.quit()
          exit()