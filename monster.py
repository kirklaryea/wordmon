import random
def PrintMonster(num_wrong):
    print()
    print("-" * 40)
    print()
    print(r" ---------------- ")
    print(r"                ")
    #these are sets of if and elifs statements that print out the figure based on the number of wrong guesses from the user
    if num_wrong ==1:
        print(r"|      __________||     |")
        print(r"|                |-|    |")
        print(r"|                |-|    |")
        print(r"|                |-|    |")
        print(r"|                |-|    |")
        print(r"|                |-|    |")
    elif num_wrong == 0:
        print(r"|                |-|    |")
        print(r"|                |-|    |")
        print(r"|                |-|    |")
        print(r"|                |-|    |")
        print(r"|                |-|    |")
        print(r"|                |-|    |")
    if num_wrong ==2:
        print(r"|    0 __________||     |")
        print(r"|   /|\          |-|    | ")
        print(r"|                |-|    |")
        print(r"|                |-|    |")
        print(r"|                |-|    | ")
        print(r"|                |-|    | ")
    elif num_wrong == 3:
        print(r"|    0 __________||     |")
        print(r"|   /|\          |-|    |")
        print(r"|    |           |-|    |")
        print(r"|                |-|    |")
        print(r"|                |-|    | ")
        print(r"|                |-|    |")
    if num_wrong == 5:
        print(r"|    0 __________||     | ")
        print(r"|   /|\          |-|    |")
        print(r"|    |           |-|    |")
        print(r"|    |           |-|    |")
        print(r"|   / \          |-|    |")
        print(r"|                |-|    |")
    elif num_wrong == 4:
        print(r"|    0 __________||     |")
        print(r"|   /|\          |-|    |")
        print(r"|    |           |-|    |")
        print(r"|    |           |-|    |")
        print(r"|                |-|    |")
        print(r"|                |-|    |")
        
    print(r"               ")
    print(r" ---------------- ")
    return num_wrong

# Loads many possible words from a file 
# and returns them as a list
# word_list = LoadWords()
def LoadWords(filename='words.txt', min_length=5):
    words = []
    with open(filename) as f:
        for word in f:
            if len(word) > min_length:
                words.append(word.rstrip())
    return words

#monster chooses a random word from the list returned in the function Loadwords, and returns the wrod in uppercases.
def getmonsterword():
 word_list=LoadWords()
 monster_word=random.choice(word_list)
 
 return monster_word.upper()
 

#asks user for input and returns the input in uppercase.
def userguess(monster_word):
  blankspace =""
  user_guess=input("Guess a letter: ")
  user_guess=user_guess.upper()
  
  return user_guess


#this function returns a string representing the word with blanks for wrong guessed letters 
# and replaces the blanks space if the guess is correct.
def blankspace(monster_word,correct_letters):
  blankspace=""
  for letter in monster_word:
   if letter in correct_letters:
      blankspace +=letter
   else:
      blankspace +="_"
  return blankspace

 
#This fucntion checks wether the letter is in the monsters random word,if true return the letter else update the figure.
def check_letter(monster_word,user_guess):
  if user_guess in monster_word:
    return True
  else:
    return False  
  

#If the the user_guess is not in the monster_word, append the letter to the list wrong_guesses
def wrong_guesses_to_list(user_guess,monster_word):
  wrong_guesses=[]
  for letter in user_guess:
    if letter not in monster_word:
      wrong_guesses.append(letter)
  return wrong_guesses   
