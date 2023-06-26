import random
import time

def play_again():
    c=input("Do you want to play again? y/Y=yes, n/N=no\n")
    if c in ['y','Y']:
        hangman()
    else:
        print("\nWe expect you to play again.\nSee you next time, come back soon.\n\n")
        exit()

def hangman():
    words = ['apple','seven','right','monkey','mango','squeeze','xmas','balloon','grapes','pineapple','swing','propose','love','magic']
    word = random.choice(words)
    length = len(word)

    chosen_word=[]
    display = []

    for i in range(length):
        display+='_'
        chosen_word += word[i] 


    limit = 5
    new=[]
    while 1:
        count=0
        time.sleep(1)
        print("The word is: ")
        print(display)
        guess_letter = input("Enter your guess letter:" )
        if guess_letter in new:
            time.sleep(1)
            print("Don't repeat the letter.....Try another letter")
            continue
        else:
            for let in range(len(chosen_word)):
                if guess_letter == chosen_word[let]:
                    display[let] = guess_letter
                    if display == chosen_word:
                        time.sleep(1)
                        print("\n\nCongratulations "+name+" ...You won!!\nThe word was -")
                        print(display)
                        print("\n\n")
                        play_again()
                    new+=guess_letter
                    count+=1
            if count == 0:
                limit-=1
                if limit==4:
                    time.sleep(1)
                    print(
                        "________\n"
                        "   |    \n")
                    print("Wrong attempt.."+ str(limit) +" attempts remaining")
                elif limit==3:
                    time.sleep(1)
                    print(
                        "________\n"
                        "   |    \n"
                        "   |    \n"
                        "   |    \n")
                    print("Wrong attempt.."+ str(limit) +" attempts remaining")
                elif limit==2:
                    time.sleep(1)
                    print(
                        "________\n"
                        "   |    \n"
                        "   |    \n"
                        "   |    \n"
                        "   O    \n")
                    print("Wrong attempt.."+ str(limit) +" attempts remaining")
                elif limit==1:
                    time.sleep(1)
                    print(
                        "________\n"
                        "   |    \n"
                        "   |    \n"
                        "   |    \n"
                        "   O    \n"
                        "  / \   \n")
                    print("Wrong attempt.."+ str(limit) +" attempts remaining")
                else:
                    time.sleep(1)
                    print(
                        "________\n"
                        "   |    \n"
                        "   |    \n"
                        "   |    \n"
                        "   O    \n"
                        "  /|\   \n"
                        "  / \   \n")
                    print("Failed\n\n")
                    play_again()
            else:
                continue
        

name=input("Enter your name:")
print("\nHello "+name+"! \nBest of Luck..!")
time.sleep(2)
print("The game is about to start...\nLet's play the game..!!")
time.sleep(3)
hangman()