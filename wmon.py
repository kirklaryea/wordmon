
import random#importing random for the monster to choose the random word
import monster#importing the module i created with functions
#to delete repository.
#go to folder
#shift+command+. to delete the whole repository.


print("Welcome to the WORD MONSTER game!A terrible monster is coming! It will only go away if we can guess all the letters in the the word it is thinking of!\nEvery letter we get wrong brings the moster closer and closer...")
 
correct_letters=[] #this list will store all correct letter chosen by the user  
wrong_guesses=[] #this list will store all wromg letter chosen by the user 
monster_word=monster.getmonsterword()#asigns the random monster word to this variable
num_wrong=0 #increments by 1 everytime the user gets the wrong guess
monster.PrintMonster(num_wrong)#updates the figure(hangman) based on the number of wrongs.
blankspace2=monster.blankspace(monster_word,correct_letters)#if the user guesses a wrong letter it return a blankspace,else if the guess is correct, it replaces the blankspace with the letter.
print(" ")
print("Wrong:" + str(wrong_guesses))#prints the wrong_guesses list
while True:
  
  print(" ")
  if blankspace2==monster_word:#if all user guesses match the monster word print yes you win.
    print("Yes, you win! ")
    break
  elif num_wrong==6:#else if the users maximizes thier attempts print "Oops you have been defeated!" and then the correct word.
    print("Oops you have been defeated!")
    print(" ")
    print("The word is: " + str(monster_word))
    break
  print(" ")
  user_guess=monster.userguess(monster_word)#assigns users guess
  if monster.check_letter(monster_word,user_guess) == True:#If the functions chcks for the letter and its True, in other words if the letter is in the monsters word, append it to the list correct letters.
    correct_letters.append(user_guess)
  else:#Else append all wrong letters to the worng_guesses list and add 1 to the num_wrong varibale.
    wrong_guesses.append(user_guess)      
    num_wrong+=1
  monster.PrintMonster(num_wrong)
    
  blankspace2=monster.blankspace(monster_word,correct_letters)
  print(blankspace2)
  print(" ")
  print("Wrong"+ str(wrong_guesses))
  print("Correct:"+ str(correct_letters))#returns a list of the users correct guesses.

