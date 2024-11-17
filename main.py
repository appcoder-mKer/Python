# main.py

# main.py
import random 
import time
from random import randint as rr
coinFlip = rr(0,1)

def printGrid(grid):

  for i in range(3):
    for j in range(3):
      if  j == 0 or j ==1:
        print(" "+grid[i][j]+" |", end ="")
      if j == 2:
        print(" "+grid[i][j], end ="")
    if i == 1 or i==0:
      print("\n---+---+---")
  print("\n")
def checkWinning(grid,player):
  if grid[0][0] == player and grid[0][1] == player and grid[0][2] == player:
    return True
  if grid[1][0] == player and grid[1][1] == player and grid[1][2] == player:
    return True
  if grid[2][0] == player and grid[2][1] == player and grid[2][2] == player:
    return True   
  if grid[0][0] == player and grid[1][0] == player and grid[2][0] == player:
    return True 
  if grid[0][1] == player and grid[1][1] == player and grid[2][1] == player:
    return True
  if grid[0][2] == player and grid[1][2] == player and grid[2][2] == player:
    return True  
  if grid[2][0] == player and grid[1][1] == player and grid[0][2] == player:
    return True   
  if grid[0][0] == player and grid[1][1] == player and grid[2][2] == player:
    return True   

  return False
  
def isWinningMove(grid, player,i,j):
  if grid[i][j] != " ":  # Check for empty cells
    return False
  else:
    grid[i][j] = player  # Make a hypothetical move
    if checkWinning(grid, player):  # Check if this leads to a win
      grid[i][j] = " "
      return True  # Return the coordinates of the winning move
  grid[i][j] = " "  # Reset the cell to empty
  return False  # No winning move found
  
def duplicateBoard(grid):
  newDupeGridOuter = []
  for i in range (3):
    newDupeGridInner = []
    for j in range(3):
      newDupeGridInner.append(grid[i][j])
    newDupeGridOuter.append(newDupeGridInner)
    
  return newDupeGridOuter
  
  
def checkFork(grid,player,i,j):
  newGrid = duplicateBoard(grid)
  if isFull(newGrid) == True:
    return False
  newGrid[i][j] = player
  numWins=0
  for n in range(3):
    for m in range(3):
      if newGrid[n][m] == " ":
        newGrid[n][m]= player
        if isWinningMove(newGrid,player,n,m)==True:
          numWins+=1
        newGrid[n][m]=" "
    
  if numWins>=2:
    return True
  else:
    return False
def oFinder(grid):
  oCoorX = 0
  oCoorY = 0
  for i in range(3):
    for j in range(3):
      if isWinningMove(grid,"o",i,j) == True:
        oCoorX = i 
        oCoorY = j
        return oCoorX, oCoorY
  for i in range(3):
    for j in range(3):
      if isWinningMove(grid,"x",i,j) == True:
        checkWinning(grid, "x") == True
        oCoorX = i
        oCoorY = j
        return oCoorX,oCoorY
  for i in range(3):
    for j in range(3):
      if(checkFork(grid,"o",i,j) == True):
        oCoorX = i
        oCoorY = j
        return oCoorX,oCoorY  
  for i in range(3):
    for j in range(3):
      if(checkFork(grid,"x",i,j) == True):
        oCoorX = i
        oCoorY = j
        return oCoorX,oCoorY      
  #block their fork, similar to how we blocked their winning move      
  if grid[1][1] == " ":
     oCoorX = 1
     oCoorY = 1
     return oCoorX,oCoorY
  corners = [[0,0],[0,2],[2,0],[2,2]]
  for i in corners:
    if grid[i[0]][i[1]] == " ":
     oCoorX = i[0]
     oCoorY = i[1]
     return oCoorX,oCoorY
  oCoorX = rr(0,2)
  oCoorX = rr(0,2)    
  while grid[oCoorX][oCoorY] != " ":
    oCoorX = rr(0,2)
    oCoorY = rr(0,2)
  return oCoorX,oCoorY 



def isFull(grid):

  for i in range (3):
    for j in range (3):
      if grid[i][j] == " ":
        return False
  return True





winnerExist = False
grid = []
for i in range (3):
  listInGrid = []
  for j in range (3):
    listInGrid.append(" ")
  grid.append(listInGrid)  

currPlayer = " "
if coinFlip == 1:
  userEnter = input("The coin fip shows the you, the user goes first. You will be playing (X)\nPress enter to begin: ")
  currPlayer = "x"
else:
  print("The coin flip shows the computer will go first, you will be playing (X)")
  currPlayer = "o"










#printGrid(grid)
while(True):
  if currPlayer == "x":
    UserRow = input("\nPick a row to play: ")
    UserCol = input("\nPick a column to play: ")
    grid[int(UserRow)][int(UserCol)] = currPlayer 
    printGrid(grid)
    if checkWinning(grid,currPlayer) == True:
      printGrid(grid)
      winnerExist = True
      break
    currPlayer = "o"
  if isFull(grid)==True:
      break
  if currPlayer == "o":
    x,y = oFinder(grid)
    grid[x][y] = currPlayer 
    printGrid(grid)
    if checkWinning(grid,currPlayer) == True:
      printGrid(grid)
      winnerExist = True
      break
    currPlayer = "x"
  if isFull(grid) == True:  
    break   
if isFull(grid)==True and winnerExist == False:
  print("It is a tie!")

else:
  print(currPlayer + " won the game!")










