# Assignment: Python Loop Statements:
print('')

# Question 1
# Task 1: Code Correction

for i in range (5,2,-1):
    print(i)

# Task 2
print('')

'''
Wrtie a program that simulates different moods for each day of the week. 
Create a list of moods. 
Using the range function , loop through the days of the week and for each day, randomly select a mood from the list and print it.
Ensure that your program inludes the Random module
'''

import random

moods = ['Happy', 'Sad', 'Energetic', 'Calm']
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

for day in days:
    mood = random.choice(moods)
    print(f"On {day}, I am feeling {mood}")
   

# Task 3
print('')

'''
Create a countdown timer that starts from 10 and counts down to 1.
Use the range() function to generate the countdown sequence. Each number should be printed on a new line.
This task will help you understand how to generate a decreasing sequence with range().
'''

time = range(10, 0, -1)

for t in time:
    print("Counting down " + str(t) + " remaining")
print("Time is up")

# Question 2
print('')

'''
Code Correction
'''

for i in range(3):
    for j in range(3):
        print("*", end=" ")
    print()

# Task 2
    print("")
'''
Simulate a mood tracker that records your mood at three different times of the day (morning, afternoon, evening)
for each day of the week.
Use nested loops to impolement this: the outer loop should iterate over the days, and the inner loop should iterate over the times of the day.
For each time, randomly select a mood from a predefined list and print it. 
'''
import random

for day in days: 
    print(f"On {day}")
    time_of_day = ['morning', 'afternoon', 'evening']
    for time in time_of_day:
        mood = random.choice(moods)
        print(f" I am feeling {mood}, during the {time}")

# Task 3
        print('')
'''
Your task is to create a multiplication table for numbers 1 through 5.
Use nested loops where the outer loop represents the multiplier and the inner loop 
represents the multiplicand.
Print the results in a tabular format.
'''        

print("Multiplication Table:")

for i in range(1, 6):    
    for j in range(1, 6):
        print(f"{i * j:2}", end=" ")  
    print()

# Question 3
# Task 1
print("")    
'''
Code Correction
'''
    
for i in range(1,11):
    if i == 5:
        continue
    print(i)

# Task 2
print('')
'''
Write a program that represents your mood swings throughout a day. 
The program should loop over each hour of the day and assign a random mood from a list for each hour.
However, at 'Lunch Time' (Which you can define as a specific hour), th eprogram shuld not print the mood. 
Use continue to achieve this behaviour. 
'''
import random

hours = range(1,25)
lunch_time = 12

for hour in hours:
    if hour == lunch_time:
        print("Lunch Time")
        continue

    mood = random.choice(moods)
    print(f"At hour {hour}, I am feeling {mood}")

# Task 3
print("")
'''
Implement a for loop that searches for a specific number in a list of numbers.
If the number is found, use break to exit the loop.
If the loop completes without finding the number, an else clause should be used to print a message stating that the number was not found.
This task will help you understand how to use the else clause in conjunction with the break statement in loops
'''

num_list = range(1,58)

for num_x in num_list:
    if num_x == 10:
        break
    else:
        print("That Number Was Not Found")

# Question 4
# Task 1
print("")
'''
Given the following code snippet, predict the output and then run the code to verify your prediction.
Explain why the output is what it is based on the placement of the increment.

marshmallows = 0
while marshmallows < 5:
    marshmallows += 1
    print("Added a marshmallow! Now there are " + str(marshmallows) + " marshmallows.")

    Output will be:
    Added a marshmallow! Now there are 1 marshmallows.
    Added a marshmallow! Now there are 2 marshmallows.
    Added a marshmallow! Now there are 3 marshmallows.
    Added a marshmallow! Now there are 4 marshmallows.
    Added a marshmallow! Now there are 5 marshmallows.

    This is the output because:
    The initial value of marshmallows is 0.
    following that declaration, the while loop states that "while marshmallows are less than 5" (zero is less than 5)
    add 1 marshmallow to marshmallows.
    following that the print statement says "Added a marshmallow! Now there are (number of marshmallows) marshmallows.
    The loop will continue to add 1 to the value of marshmallows every time that it loops until it reaches 5 marshmallows. 
'''

# Task 2
'''
Modify the code from task 1 by moving the increment operation to the end of the loop.
Predict what the ouptput will be and then run the code to check your prediciton. 
Discuss the differences in the output and how the placement of the increment affects the loop's behavior.
'''

marshmallows = 0
while marshmallows < 5:
    print("Added a marshmallow! Now there are " + str(marshmallows) + " marshmallows.")
    marshmallows += 1

'''
The output will be:
Added a marshmallow! Now there are 0 marshmallows.
Added a marshmallow! Now there are 1 marshmallows.
Added a marshmallow! Now there are 2 marshmallows.
Added a marshmallow! Now there are 3 marshmallows.
Added a marshmallow! Now there are 4 marshmallows.

The reason that the output now starts with zero is becuase the print statement is before the increment operation.
This causes the print statement to state the value of marshmallows before it has been modified.
Likewise, now the ouptut stops at 4 because it needs to be less than 5 and only increments to 5 after the print statement.
'''

# Task 3
print("")
'''
Off-by-one error investigation
Create a while loop where an off-by-one error could occur due tro the placement of the increment operation.
Your loop should aim to fill a bag with exactly 10 marshmallows, but due to the off by one error, it either has too few or too many.
Correct the error and explain the importance of increment placement in preventing such errors.
'''

# Off by one (Not enough marshmallows)
marshmallows = 0

while marshmallows < 10:
    print("Added a marshmallow! Now there are " + str(marshmallows) + " marshmallows.")
    marshmallows += 1

print(" ")

# correct:
marshmallows = 0

while marshmallows < 10:
    marshmallows += 1
    print("Added a marshmallow! Now there are " + str(marshmallows) + " marshmallows.")

'''
The incrment statement has to be placed before the print statement to output the correct numbers
so that the answer makes sense.
'''

# Question 5

# Task 1

print('')
'''
Write a while loop with a condition that will never be true (an infinite loop).
Inside the loop, print a statement. 
Then, use a break statement to exit the loop after 5 iterations.  
Explain the role of the loop condition and the break statement in controlling the loop execution.
'''

count = 0

while True:  # Infinite loop with condition that is always true
    print("Inside the loop")
    count += 1
    
    if count == 5:
        break  # Exit the loop after 5 iterations
'''
The while True: statement creates an infinite loop because the condition True is always true. 
This means that the loop will continue executing indefinitely until interrupted or until a break statement is encountered.
Inside the loop, we print the statement "Inside the loop" on each iteration.
We also have a counter variable count that keeps track of the number of iterations.
We use an if statement to check if the value of count is equal to 5. 
When count reaches 5, the break statement is executed, which exits the loop, breaking out of the loop's execution flow.
The loop condition (True) ensures that the loop continues indefinitely until the break statement is encountered. 
Once the break statement is executed, the loop terminates, and the program moves on to the next statement after the loop.
So, the loop condition (True) controls the indefinite execution of the loop, while the break statement provides a way to exit 
the loop after a certain condition (in this case, after 5 iterations) is met. Together, they allow us to execute the loop for 
a specific number of iterations within an otherwise infinite loop.
'''

# Task 2

'''
Conditional Exit
Modify the infinite loop from task 1 to include a condition that will eventually be true and remove the break statement.
The loop should terminate naturally oncce the condition is met. 
Discuss how the loop condition determines when the loop exits.
'''
print('')

count = 0
loop_condition = True

while loop_condition:
    print("Inside the loop")
    count += 1
    
    if count == 5:
        loop_condition = False 

# Task 3
print("")

'''
Create a while loop that continues to run as long as multiple conditions are true. 
Use the and or the or operators to combine conditions.
Describe how combining conditions can create more complex loop behaviors.
'''
x = 0
y = 5

while x < 10 and y > 0:
    print(f"x: {x}, y: {y}")
    x += 1
    y -= 1

'''
In this code, the loop will continue running as long as both conditions x < 10 and y > 0 are true.
By combining conditions with logical operators, you can create loops with more nuanced behavior, 
allowing you to control when the loop should continue or stop based on multiple criteria simultaneously. 
This flexibility is particularly useful for implementing complex control flow logic in your programs.
'''

# Question 6
print('')

# Task 1
'''
Write a while loop that attempts to find a specific value in a list. Use an else clause to print a 
message if the value is not found. 
Explain how the else clause works with the while loop.
'''

numbers = [10, 20, 30, 40, 50]
target = 25

found = False
index = 0

while index < len(numbers):
    if numbers[index] == target:
        print(f"Found {target} at index {index}.")
        found = True
        break
    index += 1
else:
    print(f"{target} not found in the list.")

'''
The else clause works with the while loop by executing only if the loop completes normally, without encountering a break statement. 
In the code above, if the loop finds the target value and breaks early, the else clause will be skipped. 
However, if the loop completes all iterations without finding the target value, the else clause will 
execute and print the message indicating that the value is not found.
'''

# Task 2

'''
Create a while loop that runs indefinitely, printing out the current time. 
Use a break statement to exit the loop if a certain condition is met (e.g., if the current time matches a target time). 
Discuss how the break statement can be used to exit a loop based on a condition.
'''

import time

target_hour = 6
target_minute = 52

while True:
    current_time = time.localtime()
    current_hour = current_time.tm_hour
    current_minute = current_time.tm_min

    print(f"Current time: {current_hour:02d}:{current_minute:02d}")

    if current_hour == target_hour and current_minute == target_minute:
        print("Target time reached. Exiting the loop.")
        break 


'''
The break statement causes the loop to terminate immediately, regardless of the loop condition. 
It allows us to exit the loop prematurely based on a condition, breaking out of the loop's execution 
flow and continuing with the next statement after the loop. 
In this case, it allows us to exit the infinite loop once the target time is reached.
'''

# Task 3
print('')
'''
Develop a while loop that iterates over a range of numbers. 
Use the continue statement to skip over specific numbers (e.g., multiples of 3) and print the rest. 
Explain the purpose of the continue statement and how it affects the loop's iteration.
'''

numb = 0

while numb < 30:
    numb += 1

    if numb % 3 == 0: 
        continue

    print(numb)

'''
The purpose of the 'continue' statement is to skip certain iterations o f a loop based on a specific condition without exiting the loop entirely.
In the code above, the 'continue' statement allows us to skip printing multipoles of '3' and proceed with the next iteration of the loop,
ensuring that only numbers that are not multiples of '3' are printed.
This helps to filter out specific values and control the flow of the loop according to requirements.
'''

# Task 4 
print("")
'''
Implement a while loop where you want to temporarily skip the implementation of a condition but plan to add more code later. 
Use the pass statement as a placeholder. 
Describe the use of pass in a loop and when it might be useful.
'''

machine_parts = 40
complete_machine = 70

while machine_parts < 80:
    machine_parts += 1

    if machine_parts == complete_machine:
        pass
    print("you have ", machine_parts, " machine parts")

'''
pass is a statment in python that is a null operation; nothing happens when it executes.
pass is very helpful to use when you need a placeholder to temporarily skip the implementation of a condition, but plan to add more code later.
'''    
# Question 7
print("")
# Task 1

'''
Using the provided code snippet, simulate rolling a six-sided die 10 times. 
Extend the simulation to keep track of how many times each number is rolled. 
After the simulation, print out the frequency of each number.
'''

import random

# Initialize a dictionary to keep track of dice roll frequencies
roll_count = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

# Simulate rolling the dice 10 times
for _ in range(10):
    dice_roll = random.randint(1, 6)
    # Update the roll_count dictionary
    roll_count[dice_roll] += 1
    print("You rolled a " + str(dice_roll) + "!")

print("---------------------")
print("Number Frequency:")
print("---------------------")

# Print out the frequency of each number
for number, frequency in roll_count.items():
    print(f"Number {number} was rolled {frequency} times.")

# Task 2
    
print("")
'''
Create a game where a player has to guess the random item picked by the computer from a list.
Use random.choice() to select the item and take the user's guess via input. 
Provide feedback on whether they guessed correctly or not.
'''

import random

while True:
    guess = input("Guess what number I'm holding up behind my back? Write any answer from 1-10: ")
    answer = random.choice(range(1,11))

    try:
        guess = int(guess)
    except:
        print("That's not a correct input, please only use numbers")
        continue
    
    if guess > 10 or guess < 1:
        print("That answer isn't from 1-10!")
        continue

    if guess == answer:
        print(f"You got it correct! I was holding up the number {answer}")
        break

    else:
        print(f"Sorry that's not the right answer, it was {answer}, try again!")

# Task 3
print("")

'''
Shuffling the Deck:
Simulate shuffling a deck of cards using random.shuffle(). 
Create a list representing a deck of cards, then shuffle it and print the shuffled deck. 
Discuss how random.shuffle() can be used in game development or other applications.
'''
import random

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
deck = []

for suit in suits:
    for rank in ranks:
        card = rank + ' of ' + suit
        deck.append(card)

while True:
    draws = input("Would you like to draw some cards? y or n: ")
    print("")

    if draws == 'y':
        random.shuffle(deck)
        hand = deck[:5]
        print("Drawn cards: ")
        print("--------------")

        for card in hand:
            print(card)
            print('')
            continue

    else:
        print("Thanks for your time")
        break
    
'''
random.shuffle() provides a convenient way to introduce randomness into your game. 
In many games, randomness plays a crucial role in generating unpredictable outcomes, creating variety, and increasing replayability. 
Shuffling elements such as cards, tiles, or game objects can add an element of surprise and challenge to gameplay that will keep
gamers coming back for more each time they play your game.
'''

# Question 8

# Task 1:

'''
Implement a number guessing game where the computer randomly selects a number within a range, and the player has to guess it. 
Use random.randint() to generate the number and give the player a hint after each incorrect guess whether their guess was too high or too low.
'''
print("")

import random

target_number = random.randint(1, 100)

print("Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 100. Can you guess it?")

num_guesses = 0

while True:
    
    guess = int(input("Enter your guess: "))
    num_guesses += 1
    
    if guess == target_number:
        print(f"Congratulations! You've guessed the correct number {target_number} in {num_guesses} guesses.")
        break
    elif guess < target_number:
        print("Too low! Try guessing a higher number.")
    else:
        print("Too high! Try guessing a lower number.")

# Task 2: 
print("")

'''
Create a magic 8 ball program that provides random advice. 
Use random.choice() to select a random response from a list of possible answers every time the user asks a question.
'''

import random

responses = [
    "It is certain.",
    "It is decidedly so.",
    "Without a doubt.",
    "Yes - definitely.",
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don't count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful."
]

print("Welcome to the Magic 8-Ball program!")
print("Ask the Magic 8-Ball a question and receive a random answer.")

while True:
    question = input("Ask a question (or type 'quit' to exit): ")
    
    if question.lower() == 'quit':
        print("Exiting the Magic 8-Ball program. Goodbye!")
        print("")
        break
    
    response = random.choice(responses)
    print("Magic 8-Ball says:", response)

# Task 3

'''
Develop a game where the computer randomly picks a card from a deck, and the player has to guess the suit or the rank. 
Use random.choice() to selct the card, and then check if the player's guess matches the suit or rank of the chosen card.
'''
import random

suits = ['hearts', 'diamonds', 'clubs', 'spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
deck = []

for suit in suits:
    for rank in ranks:
        card = rank + ' of ' + suit
        deck.append(card)

while True:
    hand = [random.choice(deck)]

    answer = input("Guess the suit or rank of a card drawn from the deck (all suit names are lowercase) : ")

    if answer in hand[0]:
        print(f"That's correct! The answer was {hand[0]}!")
    else:
        print(f"Sorry, that's incorrect. The answer was {hand[0]}.")

    draw_again = input("Would you like to guess another card? (y/n): ")
    if draw_again != 'y':
        print("Thanks for playing!")
        print("")
        break
    else:
        continue

# Question 9:
    
# Task 1

'''
Using the provided genres list, write a for loop that prints out each genre with a custom message. 
Extend this task by adding a counter that displays the number of the track before the genre
'''    
# Task 2

'''
Convert the for loop from Task 1 into a while loop. 
Ensure it performs the same function but also includes a condition to stop the loop if a certain genre is played.
'''

# Task 3
'''
Using the range() function, loop through the genres list by index. 
For each genre, print out the track number and a message that the light show is ready. 
Modify the loop to skip a genre if it's not suitable for the light show.
'''

# Question 10:

# Task 1

'''
Loop through a slice of the genres list and print only the selected genres. Use slicing to create a sublist of genres from the second to the fourth track.

# Selective playlist slice
selected_genres = genres[1:4]  # From Rock to Classical

# Loop through the selected slice
for genre in selected_genres:
    print("Selective play: " + genre)

'''

# Task 2

'''
Use a list comprehension to create a new list that contains each genre with the word "Music" appended to it. Print this new list.

# List comprehension to append "Music" to each genre
music_genres = [genre + " Music" for genre in genres]
print(music_genres)

'''

# Task 3

'''
Write a loop using range() to print out a countdown from 10 to 1, followed by the message "The beat drops now!".

# Countdown with range
for number in range(10, 0, -1):
    print(number)
print("The beat drops now!")

'''


# CODE for Q 9 and 10 ------------------------------------------------------------
import random

# Our playlist of genres
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
unsuitable_genre = 'Classical'

# Shuffle the genres
random.shuffle(genres)

# Countdown with range
for number in range(10, 0, -1):
    print(number)
print("The beat drops now!")

# Custom messages for each genre
custom_messages = {
    'Jazz': "Let the smooth sounds of Jazz take you on a journey!",
    'Rock': "Get ready to rock out with the best hits of Rock music!",
    'Hip-hop': "Feel the rhythm and groove to the beats of Hip-hop!",
    'Classical': "Experience the timeless elegance of Classical music!"
}

# Keep the party alive until we've reached the end or the unsuitable_genre
for index in range(len(genres)):
    if genres[index] == unsuitable_genre:
        continue  # Skip the light show for this genre
    genre = genres[index]
    print(f"Track {index + 1}: {custom_messages[genre]} - Light show is on!")

# Selective playlist slice
selected_genres = genres[1:4]  # From Rock to Classical

# Loop through the selected slice
for genre in selected_genres:
    print("Selective play: " + genre)

# Initialize an empty list to store genres with "Music" appended
music_genres = []

# Append "Music" to each genre and add it to the music_genres list
for genre in genres:
    music_genre = genre + " Music"
    music_genres.append(music_genre)

# Print the new list containing genres with "Music" appended
print(music_genres)
