# game.py

import random
from data import suspects, locations, weapons
from ai_assistant import get_clue_openai

# Developer cheat code
CHEAT_CODE = "pancakes"

def print_intro():
    print("\n🎬 WELCOME TO MURDER IN HOLLYWOOD")
    print("A murder has occurred on set. You're the detective. Sadly, your assistant is... Clarence.")
    print("Ask for clues. Eliminate suspects, locations, and weapons. Then make your accusation.")
    print("Type 'clue' for a clue, 'accuse' to solve the murder, 'exit' to quit.\n")

def print_matrix(remaining):
    print("\n🕵️ Remaining Possibilities:")
    print("Suspects:", ', '.join(remaining['suspects']))
    print("Locations:", ', '.join(remaining['locations']))
    print("Weapons:", ', '.join(remaining['weapons']))
    print()

def get_player_choice():
    return input(">>> What do you want to do? (clue / accuse / exit): ").strip().lower()

def get_accusation():
    print("\n🔎 Make your final accusation.")
    s = input("Suspect: ").strip()
    l = input("Location: ").strip()
    w = input("Weapon: ").strip()
    return s, l, w

def main():
    solution = {
        "suspect": random.choice(suspects),
        "location": random.choice(locations),
        "weapon": random.choice(weapons)
    }

    eliminated = []
    remaining = {
        "suspects": suspects.copy(),
        "locations": locations.copy(),
        "weapons": weapons.copy()
    }

    print_intro()

    while True:
        choice = get_player_choice()

        if choice == "exit":
            print("Thanks for playing. Clarence will now judge you in silence.")
            break

        elif choice == "clue":
            clue = get_clue_openai((solution["suspect"], solution["location"], solution["weapon"]), eliminated)
            print(f"\n🤖 Clarence: {clue}\n")

        elif choice == CHEAT_CODE:
            print(f"\n👨‍💻 DEV CHEAT ENABLED:")
            print(f"The real solution is: {solution['suspect']} in the {solution['location']} with the {solution['weapon']}.\n")

        elif choice == "accuse":
            s, l, w = get_accusation()

            # Eliminate guessed items from the matrix
            for cat, guess, full in [("suspects", s, suspects), ("locations", l, locations), ("weapons", w, weapons)]:
                if guess in remaining[cat]:
                    remaining[cat].remove(guess)
                eliminated.append(guess)

            if (s == solution["suspect"] and l == solution["location"] and w == solution["weapon"]):
                print("\n🎉 You got it! The mystery is solved. Clarence begrudgingly respects you... slightly.")
                break
            else:
                print("\n❌ That's not it. Clarence rolls his eyes and sighs so loudly it echoes in the studio.\n")
                print_matrix(remaining)

        else:
            print("Invalid input. Type 'clue', 'accuse', or 'exit'. Or try... 'pancakes'? 😉")

if __name__ == "__main__":
    main()
