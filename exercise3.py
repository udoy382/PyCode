# Python Exercise3 Guess The Number #20

#       its my own maker.
# n = 6

# while(True):
#     x = int(input("Enter the number\n"))
#     if x>n:
#         print("nahin or kam karo")
#     elif x==n:
#         print("Congratulation")
#         break
#     else:
#         print("nahin or jada karo")


#       Comments project.

n = 18
number_of_guesses=1
print("Number of guesses is limited to only 9 times:")
while(number_of_guesses<=9):
    Guess_number = int(input("Guess the number:\n"))
    if Guess_number<18:
        print("you enter less number please input greater number.\n")
    elif Guess_number>18:
        print("you enter greter number please input smaller nuber:\n")
    else:
        print("you won\n")
        print("number_of_guesses, no of guesses left")
        break
    print(9-number_of_guesses,"no of guesses left")
    number_of_guesses=number_of_guesses+1

    if(number_of_guesses>9):
#         print("Game Over")