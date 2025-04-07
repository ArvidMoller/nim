import random

def stacks(stack_num, stick_num):
    stack_arr = [0] * stack_num

    i = 0
    while i < len(stack_arr):
        stack_arr[i] = random.randint(1, stick_num - stack_num)

        if i == len(stack_arr)-1:
            stack_arr[i] = stick_num

        stick_num -= stack_arr[i]
        stack_num -= 1
        i += 1

    return stack_arr 
    

def binarize_arr(arr):
    rArr = []
    longest = 0
    for i in arr:
        rArr.append(bin(i).replace("0b", ""))
        if len(bin(i).replace("0b", "")) > longest:
            longest = len(bin(i).replace("0b", ""))

    i = 0
    while i < len(rArr):
        while len(rArr[i]) < longest:
            rArr[i] = "0" + rArr[i]
        i += 1

    return rArr


def xor_sum(arr):
    arr = binarize_arr(arr)

    sum = ""
    one_arr = [0] * len(arr[0])

    i = 0
    while i < len(arr):
        j = 0
        while j < len(arr[i]):
            if arr[i][j] == "1":
                one_arr[j] += 1
            j += 1
        i += 1
    
    i = 0
    while i < len(one_arr):
        if one_arr[i]%2 == 0:
            sum += "0"
        else:
            sum += "1"
        i += 1
        
    return int(sum, 2)


def best_move(stack_arr):
    stack = 0
    while stack < len(stack_arr):
        for move in range(1,4):
            print(move)
            tmp_arr = stack_arr.copy()
            if tmp_arr[stack] - move >= 0:
                tmp_arr[stack] -= move 
                if xor_sum(tmp_arr) == 0:
                    print(xor_sum(tmp_arr))
                    return stack, move
                
                if tmp_arr[stack] - move > 0:
                    possible_move = [stack, move]
        stack+=1
    
    return possible_move


def player_input(stack_arr, stack_num):
    while True:
        try:
            stack = int(input(f"Vilken hög vill du spela från? (1-{stack_num}) \n"))
            if stack in range(1, stack_num+1) and stack_arr[stack-1] > 0:
                break
            else:
                print("Ogiltigt drag. Försök igen.")
        except ValueError:
            print(f"Ange en siffra mellan 1 och {stack_num}.")

    while True:
        try:
            move = int(input("Hur många pinnar vill du ta? (1-3) \n"))
            if move in range(1, 4) and move <= stack_arr[stack-1]:
                break
            else:
                print("Ogiltigt drag. Försök igen.")
        except ValueError:
            print("Ange en siffra mellan 1 och 3.")

    return stack, move


def play_against_human(stack_arr, stack_num):
    player_turn = random.choice([1, 2])  # Startspelare
    
    while sum(stack_arr) > 0:
        print(f"\nDet är spelare {player_turn}s tur.")
        print(f"{stack_arr} pinnar kvar i varje hög.")

        stack, move = player_input(stack_arr, stack_num)
        
        if sum(stack_arr) == 0:
            print(f"Spelare {player_turn} tog sista pinnen och förlorade!")
            break

        stack_arr[stack-1] -= move
        
        if sum(stack_arr) == 0:
            print(f"Spelare {player_turn} tog sista pinnen och förlorade!")
            break
        
        # Byt spelare
        player_turn = 2 if player_turn == 1 else 1


def play_against_computer(stack_arr, stack_num): 
    while sum(stack_arr) > 0:
        print(f"\nDet är din tur.")
        print(f"{stack_arr} pinnar kvar i varje hög.")

        stack, move = player_input(stack_arr, stack_num)
        
        stack_arr[stack-1] -= move

        if sum(stack_arr) == 0:
            print(f"Du tog sista pinnen och förlorade!")
            break

        move_arr = best_move(stack_arr)
        stack_arr[move_arr[0]] -= move_arr[1]
        print(f"\nDatorn tar {move_arr[1]} pinnar från hög nummer {move_arr[0]+1}.")
        
        if sum(stack_arr) == 0:
            print(f"Datorn tog sista pinnen och förlorade!")
            break

def nim_game():
    print("Välkommen till Nim!")

    while True:
        try:
            stick_num = int(input("Hur många pinnar vill du spela med (21 rekommenderas)?\n"))
            if stick_num in range(9, 100):
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

    stack_arr = stacks(stack_num, stick_num)

    while True:
        opponent = input("Vill du spela mot en annan männsika? (y/n)\n")
        if opponent in ["y", "n"]:
            break
        else:
            print("Ogiltigt svar, svar y eller n")

    if opponent == "y":
        play_against_human(stack_arr, stack_num)
    else:
        play_against_computer(stack_arr, stack_num)
        
    
# Starta spelet
if __name__ == "__main__":
    nim_game()