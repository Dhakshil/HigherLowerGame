import art
import random
import GameData
import os

count = 0

while True:

    def get_data1():
        random_dict = random.choice(GameData.data)
        return random_dict


    def get_data2():
        random_dict = random.choice(GameData.data)
        return random_dict


    my_dict1 = get_data1()
    my_dict2 = get_data2()

    print(art.logo)
    if my_dict1 == my_dict2:
        break
    question1 = f"Compare A: {my_dict1['name']}, a {my_dict1['description']} from {my_dict1['country']}"

    question2 = f"Against B: {my_dict2['name']}, a {my_dict2['description']} from {my_dict2['country']}"

    print(question1)
    print(art.vs)
    print(question2)

    user_input = input("Who has more followers? Type 'A' or 'B': ").lower()
    count += 1
    followers1 = my_dict1['follower_count']
    followers2 = my_dict2['follower_count']

    if user_input == 'a':
        if followers1 > followers2:
            print(f"You're right! Current score: {count}")
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            count -= 1
            print(f"Sorry, that's wrong. Final score: {count}")
            break
    elif user_input == 'b':
        if followers2 > followers1:
            print(f"You're right! Current score: {count}")
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            count -= 1
            print(f"Sorry, that's wrong. Final score: {count}")
            break
    else:
        None
