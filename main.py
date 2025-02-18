import random
import art


cards = [11, 1, 2, 3,4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def play_blackjack():
    print(art.logo)
    play_again = True
    another_card = True
    while play_again:
        # user_random_card1 = random.choice(cards)
        # user_random_card2 = random.choice(cards)
        # computer_random_card1 = random.choice(cards)
        # computer_random_card2 = random.choice(cards)
        user_cards = []
        computer_cards = []

        for _ in range(2):
            user_cards.append(random.choice(cards))
            computer_cards.append(random.choice(cards))

        computer_total = sum(computer_cards)


        print(f"Your cards are: {user_cards}")
        print(f"The computers random card is {computer_cards[0]}")

        while sum(computer_cards) <= 14:
            computer_cards.append(random.choice(cards))
            computer_total = sum(computer_cards)

        while another_card:
            choice = str(input("Do you want to get another card? Type 'y' or 'n'\n")).lower()
            user_total = sum(user_cards)
            if choice == 'y':
                user_cards.append(random.choice(cards))
                print(f"Your cards are: {user_cards}")
            elif choice == 'n':
                if user_total > 21:
                    print("Bust. You lose")
                    another_card = False
                elif user_total == computer_total:
                    print("It was a draw")
                    another_card = False
                else:
                    if user_total > computer_total or user_total == 21 or computer_total > 21:
                        print("Congratulations. You win")
                        another_card = False
                    else:
                        print("You lose")
                        another_card = False

                print(f"Your cards total were {user_total} and the computers cards totaled {computer_total}")
                print(f"Your cards were: {user_cards}\nThe computers cards were: {computer_cards}")
            else:
                print("If you can't follow the rules, you can't play anymore. Goodbye")
                quit()
        keep_playing = str(input("Do you want to play again? Type 'y' to play again or 'n' to quit:\n"))
        if keep_playing == 'y':
            print("GREAT! Here are your new cards.")
            print("\n"*20)
            play_blackjack()
            #play the game again using a function call. Maybe recursive
        else:
            print("It was nice having you here. Come again sometime")
            play_again = False
            quit()

play_blackjack()