import random

def stacks(stack_num, stick_num):
    stack_arr = [0] * stack_num

    i = 0
    while i < len(stack_arr):
        print(f"rand: {stick_num - stack_num}")
        stack_arr[i] = random.randint(1, stick_num - stack_num)
        print(i)

        if i == len(stack_arr)-1:
            stack_arr[i] = stick_num
            print("JA")

        stick_num -= stack_arr[i]
        i += 1

    return stack_arr 


    


def nim_game():
    print("Välkommen till Nim!")

    while True:
        try:
            stick_num = int(input("Hur många pinnar vill du spela med (21 rekommenderas)?\n"))
            if stick_num in range(10, 100):
                break
            else:
                print("Ogiltigt antal pinnar")
        except ValueError:
            print("Ogiltigt svar, skriv en siffra mellan 10-100")

    while True:
        try:
            stack_num = int(input("Hur många högar vill du spela med (3 rekommenderas)?\n"))
            if stack_num in range(1, 10) and stick_num/stack_num >= 1:
                break
            else:
                print("Ogiltigt antal högar")
        except ValueError:
            print("Ogiltigt svar, skriv en siffra mellan 1-10")
        
    
    player_turn = random.choice([1, 2])  # Startspelare


    
    while stick_num > 0:
        print(f"\nDet är spelare {player_turn}s tur.")
        while True:
            try:
                move = int(input("Hur många pinnar vill du ta? (1-3): "))
                if move in [1, 2, 3] and move <= stick_num:
                    break
                else:
                    print("Ogiltigt drag. Försök igen.")
            except ValueError:
                print("Ange en siffra mellan 1 och 3.")
        
        stick_num -= move
        print(f"{stick_num} pinnar kvar.")
        
        if stick_num == 0:
            print(f"Spelare {player_turn} tog sista pinnen och förlorade!")
            break
        
        # Byt spelare
        player_turn = 2 if player_turn == 1 else 1


# # Starta spelet
# if __name__ == "__main__":
#     nim_game()


print(stacks(3, 9))