#Python3
import random
import math
# Taking Inputs
lower = int(input("Enter Lower bound:- "))
 
# Taking Inputs
upper = int(input("Enter Upper bound:- "))
 
# generating random number between
# the lower and upper
x = random.randint(lower, upper)
print("\n\tYou've only ",
       round(math.log(upper - lower + 1, 2)),
      " chances to guess the integer!\n")
 
# Initializing the number of guesses.
count = 0
 
# for calculation of minimum number of
# guesses depends upon range
while count < math.log(upper - lower + 1, 2):
    count += 1
 
    # taking guessing number as input
    guess = int(input("Guess a number:- "))
 
    # Condition testing
    if x == guess:
        print("Congratulations you did it in ",
              count, " try")
        # Once guessed, loop will break
        break
    elif x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You Guessed too high!")
 
# If Guessing is more than required guesses,
# shows this output.
if count >= math.log(upper - lower + 1, 2):
    print("\nThe number is %d" % x)
    print("\tBetter Luck Next time!")
 
# Better to use This source Code on pycharm!
#C
#include<stdio.h>
#include<stdlib.h>
#include<time.h>
 
int main()
{
    int number, guess, nguesses=1;
    srand(time(0));
   
    // Generates a random number between 1 and 100
    number = rand()%100 + 1;
    
    // printf("The number is %d\n", number);
    // Keep running the loop
    // until the number is guessed
    do
    {
        printf("Guess the number between 1 to 100\n");
        scanf("%d", &guess);
        if(guess>number)
        {
            printf("you guessed to high\n");
        }
        else if(guess<number)
        {
            printf("you guessed too low\n");
        }
        else
        {
            printf("You guessed the correct number");
            printf("attempts : %d\n", nguesses);
        }
        nguesses++;
    } while(guess!=number);
     
    return 0;
}
// this code is provided by harsh sinha username- harshsinha03
