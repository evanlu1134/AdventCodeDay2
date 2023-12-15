# --- Part Two ---
# Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

# Equipped with this new information, you now need to find the real first and last digit on each line. For example:

# two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen
# In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.


def readfile(filename):
  with open(filename, "r") as f:
    return [line.rstrip("\n") for line in f]

inputLine = readfile("input.txt")
exLine = readfile("ex.txt")
exTwoLine = readfile("exD2.txt")
inTwoLine = readfile("inD2.txt")
# print(inputLine)

# def translate(text):
#   word = ""
#   for char in text:
#     word += char
#     if "one" in word:
#       text = text.replace("one","1")
#     if "two" in word:
#       text = text.replace("two","2")
#     if "three" in word:
#       text = text.replace("three","3")
#     if "four" in word:
#       text = text.replace("four","4")
#     if "five" in word:
#       text = text.replace("five","5")
#     if "six" in word:
#       text = text.replace("six","6")
#     if "seven" in word:
#       text = text.replace("seven","7")
#     if "eight" in word:
#       text = text.replace("eight","8")
#     if "nine" in word:
#       text = text.replace("nine","9")
#   return text
  
def translate(text):
  result = ""
  str = ""
  for i,char in enumerate(text):
    str += char
    if char.isdigit(): 
      result += char
    if "one" in str:
      result += "1"
      str = str[-1]
    if "two" in str:
      result += "2"
      str = str[-1]
    if "three" in str:
      result += "3"
      str = str[-1]
    if "four" in str:
      result += "4"
      str = str[-1]
    if "five" in str:
      result += "5"
      str = str[-1]
    if "six" in str:
      result += "6"
      str = str[-1]
    if "seven" in str:
      result += "7"
      str = str[-1]
    if "eight" in str:
      result += "8"
      str = str[-1]
    if "nine" in str:
      result += "9"
      str = str[-1]
  return result


#issue
# print(translate("twone")) #21 not 22
def calculate(arr):
  valsList = []
  
  for vals in arr:
    currVal = ""
    for num in vals:
      if num.isdigit(): currVal += num
    valsList.append(currVal)

  result = 0
  for digits in valsList:
    if len(digits) > 2:
      start = digits[0]
      end = digits[-1]
      total = start + end
      result += int(total)
    elif len(digits) == 1:
      double = digits + digits
      result += int(double)
    else:
      result += int(digits)

  return result


def solution(textList):
  resultList = []
  for strings in textList:
    resultList.append(translate(strings))
  print(resultList)
  return calculate(resultList)
  
# print(solution(exLine))
# print(solution(inputLine))

# ================================================




# --- Day 2: Cube Conundrum ---
# You're launched high into the atmosphere! The apex of your trajectory just barely reaches the surface of a large island floating in the sky. You gently land in a fluffy pile of leaves. It's quite cold, but you don't see much snow. An Elf runs over to greet you.

# The Elf explains that you've arrived at Snow Island and apologizes for the lack of snow. He'll be happy to explain the situation, but it's a bit of a walk, so you have some time. They don't get many visitors up here; would you like to play a game in the meantime?

# As you walk, the Elf shows you a small bag and some cubes which are either red, green, or blue. Each time you play this game, he will hide a secret number of cubes of each color in the bag, and your goal is to figure out information about the number of cubes.

# To get information, once a bag has been loaded with cubes, the Elf will reach into the bag, grab a handful of random cubes, show them to you, and then put them back in the bag. He'll do this a few times per game.

# You play several games and record the information from each game (your puzzle input). Each game is listed with its ID number (like the 11 in Game 11: ...) followed by a semicolon-separated list of subsets of cubes that were revealed from the bag (like 3 red, 5 green, 4 blue).

# For example, the record of a few games might look like this:

# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
# In game 1, three sets of cubes are revealed from the bag (and then put back again). The first set is 3 blue cubes and 4 red cubes; the second set is 1 red cube, 2 green cubes, and 6 blue cubes; the third set is only 2 green cubes.

# The Elf would first like to know which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?

# In the example above, games 1, 2, and 5 would have been possible if the bag had been loaded with that configuration. However, game 3 would have been impossible because at one point the Elf showed you 20 red cubes at once; similarly, game 4 would also have been impossible because the Elf showed you 15 blue cubes at once. If you add up the IDs of the games that would have been possible, you get 8.

# Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?

#rule contained only 12 red cubes, 13 green cubes, and 14 blue cubes?
# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# def combine(listRounds,listVals,listColor):

#   blue = 0
#   red = 0
#   green = 0

#   for i in range(len(listColor)):

#     currRounds = listRounds[i]
#     notReset = listRounds[i - 1]
#     currColors = listColor[i]
#     currVals = listVals[i]
    
#     if currColors == "green":
#       green += int(currVals)
#     if currColors == "red":
#       red += int(currVals)
#     if currColors == "blue":
#       blue += int(currVals)
#     # if(currRounds != notReset):
#     #   blue = 0
#     #   red = 0
#     #   green = 0

#     # print(currRounds,green,red,blue)
      
      

# def gameJudge(game):
#   recordVals = []
#   recordColors = []
#   recordRounds = []
#   startGame = False
#   isVal = True
#   count = 0
#   for round in game:
#     vals = ""
#     colors = ""
#     count+=1
#     for i,record in enumerate(round):
      
#       if record == ":":
#         startGame = True
#       if startGame == True:
#         if record.isdigit():
#           vals += record
#           if len(colors) > 0:
#             if colors != "Game": (recordRounds.append(count),recordColors.append(colors))
#             colors = ""
#         if record.isalpha():
#           print(i,record)
#           colors += record
#           if len(vals) > 0:
#             recordVals.append(vals)
#             vals = ""
#   print(recordColors)
#   return combine(recordRounds,recordVals,recordColors)
  # return (recordVals,recordColors)
# print(gameJudge(exTwoLine))

def calcGames(gameList):
  blue = 0
  red = 0
  green = 0
  end = 0
  for i, roundsLists in enumerate(gameList):
    gameCount = i + 1
    for j, rounds in enumerate(roundsLists):
      for x, record in enumerate(rounds):
        total = 0
        digits = ""
        for y,letters in enumerate(record):
          # print(y,letters)
          if letters.isdigit():
            digits += letters
          if letters == "b" or letters == "b" or letters == "b":
              total += int(digits)
              digits = ""
          if letters == "b":
            blue += total
          if letters == "r":
            red += total
          if letters == "g":
            green += total
          # print(blue,red,green)
          if y == len(record) - 1:
            if red > 12 and green > 13 and blue > 14:
              validGame = False
            red = 0
            green = 0
            blue = 0

            
  return end
# 12 red cubes, 13 green cubes, and 14 blue cubes?
def defineGame(games):
  recordList = []
  
  for game in games:
    startGame = False
    word = ""
    gameLists = []
    for i,char in enumerate(game):
      if char == ":":
        startGame = True
      if startGame == True:
        if char == ":" : continue
        word += char
        if char == ";":
          gameLists.append([word[:len(word) - 1]])
          word = ""
        if i == len(game) - 1: 
          gameLists.append([word])
          recordList.append(gameLists)

  return calcGames(recordList)

print(defineGame(exTwoLine))
# print(defineGame(inTwoLine))
