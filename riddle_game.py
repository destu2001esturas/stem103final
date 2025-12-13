import random

#Inspect the users answers.
def inspect_answer(the_user_guess, real_answer):
    """
    Inspect the users answer if they got it correct.
    """
    if the_user_guess.lower().strip() == real_answer.lower().strip():
        return True
    else:
        return False

def play_riddle_game():
    """
    These questions are from past events and pop cultures.
    """
    #variables
    riddles = [
        ("He always use iron sights instead of a scope during the winter war?", "Simo Hayha"),
        ("He has a white feather on his bush hat during the vietnam war?", "Carlos Hathcock"),
        ("He was responsible for the great leap forward and the cultural revolution?", "Mao Zedong"),
        ("He survived two atomic bombs that were dropped on Hiroshima and Nagasaki to end WW2?", "Tsutomu Yamaguchi"),
        ("A Bosnian Serb civilian, assassinated Archduke Franz Ferdinand and his wife. Which caused WW1?", "Gavrilo Princip"),
        ("In the movie wanted is it possible to perform a curve shot in real life?", "no"),
        ("In the minecraft movie there is a pig with a crown on it's head to honor a youtuber who passed away?", "technoblade"),
        ("What does saja mean, form a boy band name in k-pop demon hunters?", "Lion"),
        ("Inside our bodies we have origins, but one is very important that's keeping us alive without it we might die?", "The Heart"),
        ("If you ever encounter a horde of 100,000,000 zombies what would you do?", "run away")
    ]

    score = 0

    print("Welcome are you ready to start?")
    print("Let's see how well you are, good luck.\n")

    #loop
    for riddle_text, answer in riddles:
        print(f"Riddle: {riddle_text}")

        the_user_guess = input("Your answer: ")

        #function and if/else statements
        if inspect_answer(the_user_guess, answer):
            print("Correct.\n")
            score += 1
        else:
            print(f"Incorrect. The real answer was '{answer}'.\n")

    #final result
    print(f"Game Over You answered {score} out of {len(riddles)}.")
    if score == len(riddles):
        print("You are a winner")
    elif score > 0:
        print("Keep trying.")
    else:
        print("Better luck next time.")

if __name__ == "__main__":
    play_riddle_game()