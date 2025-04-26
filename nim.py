import random


# Beskrivning: Denna funktion fördelar alla pinnar i högar genom att först lägga en pinne i varje hög och sedan iterera över alla högar och lägga ett random antal pinnar i varje hög.
#
# Argument:
# stack_num: Anatl högar som ska skapas.
# stick_num: Antal pinnar som ska delas upp i högar.
#
# Return: 
# rArr: En array med antalet pinnar i varje hög. [antal pinnar i hög 1, antal pinnar i hög 2, antal pinnar i hög 3, osv.]
#
# Exempel: 
# stacks(3, 21) => [5, 10, 6]
# stacks(2, 10) => [4, 6]
# stacks(5, 30) => [5, 10, 6, 5, 4]
#
# Datum: 2025-04-26
# Namn: Arvid Möller
def stacks(stack_num, stick_num):
    stack_arr = [1] * stack_num
    stick_num -= stack_num

    while stick_num > 0:
        i = random.randint(0, stack_num-1)
        stack_arr[i] += 1
        stick_num -= 1

    return stack_arr
    

# Beskrivning: Denna funktion omvandlar alla tal i en array till binära tal, samt normaliserar dem i längd och tar bort "0b" prefixet. Detta sker genom  att iterera genom arr och omvandla varje element till binärt, samt byta ut "0b" til inget med .replace(). Längden på varje binärt tal kollas också, längden av det största talet sparas i longest. Sedan itererar jag genom arrayen med alla binära tal (rArr) och lägger till nollor i början på alla tal som är kortare än longest. 
#
# Argument:
# arr: Arrayen som med tal som ska bli binära.
#
# Return: 
# rArr: En array med normaliserade, binära tal. 
#
# Exempel: 
# binarize_arr([1, 2, 3, 4]) => ['001', '010', '011', '100']
# binarize_arr([10, 2, 32, 11]) => ['001010', '000010', '100000', '001011']
# binarize_arr([1, 7, 12, 100]) => ['0000001', '0000111', '0001100', '1100100']
#
# Datum: 2025-04-26
# Namn: Arvid Möller
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


# Beskrivning: Denna funktion räknar ut xor summan eller nim summan för antalet pinnar i varje hög. Detta innebär att arrayen med antalet pinnar i varje hög blir omvandlas från tal med basen 10 till binära tal. Sedan räknas alla 1or på varje position hos de binära talen. Om antelet 1or på en position är jämnt blir talet på den platsen i summan 0, annars blir den 1. Denna binära xor-summa omvandlas sedan till bas 10 och retuneras.  
#
# Argument:
# arr: En array med antalet pinnar i varje hög i nim spelet. 
#
# Return: 
# int(sum, 2): Xor-summan för antalet pinnar i varje hög i basen 10.
#
# Exempel: 
# xor_sum([1, 2, 3, 4]) => 4
# xor_sum([10, 2, 32, 11]) => 35
# xor_sum([1, 7, 12, 100]) => 110
# 
#
# Datum: 2025-04-26
# Namn: Arvid Möller
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


# Beskrivning: Denna funktion hittar det bästa draget geonom att iterera genom alla möjliga drag och checka den nya xor-summan. När ett drag som ger summan 0 hittas retuneras draget. Om inget darg skulle hittas returneras det senaste draget datorn kolla på som gick att spela.  
#
# Argument:
# stack_arr: En array med anatlet pinnar i varje hög. 
#
# Return: 
# stack: Vilken hög datorn ska spela från.
# move: Hur många pinnar datorn ska ta från högen.
# possible_move: En array med följande struktur: [stack, move]. Innehåller det senaste darget som GÅR att spela, används om datorn inte skulle hitta ett darg som ger xor-summan 0. 
#
# Exempel: 
# best_move([1, 2, 3, 4]) => [3, 4]
# best_move([10, 2, 32, 11]) => [2, 29]
# best_move([6, 3, 9]) => [2, 4]
#
# Datum: 2025-04-26
# Namn: Arvid Möller
def best_move(stack_arr):
    stack = 0
    while stack < len(stack_arr):
        for move in range(1, stack_arr[stack]+1):
            tmp_arr = stack_arr.copy()
            if tmp_arr[stack] - move >= 0:
                tmp_arr[stack] -= move 
                if xor_sum(tmp_arr) == 0:
                    return stack, move
                elif tmp_arr[stack] - move >= 0:
                    possible_move = [stack, move]
        stack+=1
    
    return possible_move


# Beskrivning: Denna fumktion tar input från en spelare och validerar spelerens input i en input loop för att kontrollera om svarenm är giltliga. Input som hämtas: Vilken hög spelaren ska spela från. Hur många pinnas som ska tas upp. 
#
# Argument:
# stack_arr: En array med hur många pinnar som finns i varje hög.
# stack_num: Hur många högar som finns.
#
# Return: 
# stack: Vilken hög spelaren vill spela från.
# move: Hur många pinnar spelaren vill ta upp. 
#
# Exempel: 
# Går inte att ge ett exakt exempel i och med att det beror helt på vad spelaren ger för input. 
#
# Datum: 2025-04-26
# Namn: Arvid Möller
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
            move = int(input(f"Hur många pinnar vill du ta? (1-{stack_arr[stack-1]}) \n"))
            if move in range(1, stack_arr[stack-1]+1) and move <= stack_arr[stack-1]:
                break
            else:
                print("Ogiltigt drag. Försök igen.")
        except ValueError:
            print(f"Ange en siffra mellan 1 och {stack_arr[stack-1]}.")

    return stack, move


# Beskrivning: Detta är spel loopen för ett spel mot en annan männsika. Datorn randomizar vilken spelare som ska börja och kör sedan player_input() för att hämta spelarens input. Datorn kontrollerar sedan om spelaren tog den sista pinnen eller inte. Om den sista pinnen tags avslutas spelet, annars byter programmet vilken splares tur det är.
#
# Argument:
# stack_arr: En array med hur många pinnar som finns i varje hög.
# stack_num: Hur många högar som finns.
#
# Return: 
# void
#
# Exempel: 
# Eftersom funktionen inte har några returns går det inte att skriva exempel.
#
# Datum: 2025-04-26
# Namn: Arvid Möller
def play_against_human(stack_arr, stack_num):
    player_turn = random.choice([1, 2])
    
    while sum(stack_arr) > 0:
        print(f"\nDet är spelare {player_turn}s tur.")
        print(f"{stack_arr} pinnar kvar i varje hög.")

        stack, move = player_input(stack_arr, stack_num)
        
        if sum(stack_arr) == 0:
            print(f"Spelare {player_turn} tog sista pinnen och vann!")
            break

        stack_arr[stack-1] -= move
        
        if sum(stack_arr) == 0:
            print(f"Spelare {player_turn} tog sista pinnen och vann!")
            break
        
        player_turn = 2 if player_turn == 1 else 1


# Beskrivning: Detta är spel loopen för ett spel mot datorn. Funktionen börjar med att kolla vad den aktuella xor-summan är, om den är 0 är datorn i en förlorande position om den börjar, däför kommer då männsikan få börja. Om xor-summan är något annat än 0 har datorn en vinnande position och börjar därför. Om männsikan spelar kommer player_input() anropas och hämta spelarens drag, sedan kommer funktionen justera antalet pinnar i varje hög, kolla om du tog sista pinnen eller inte och slutligen byta spelare. När datorn spelar kommer best_move() anropas. Den funktionen kommer räkna ut det bästa draget och returnera det. Därefter kommer det dreget spelas, funktionen kommer kolla om datorn tog den sista pinnen eller inte och slutligen byta spelare.  
#
# Argument:
# stack_arr: En array med hur många pinnar som finns i varje hög.
# stack_num: Hur många högar som finns.
#
# Return: 
# void
#
# Exempel: 
# Eftersom funktionen inte har några returns går det inte att skriva exempel.
#
# Datum: 2025-04-26
# Namn: Arvid Möller
def play_against_computer(stack_arr, stack_num): 
    if xor_sum(stack_arr) != 0:
        current_player = "computer"
        print("\nDatorn startar!")
    else:
        print("\nDu startar!")
        current_player = "human"

    while sum(stack_arr) > 0:
        if current_player == "human":
            print(f"\nDet är din tur.")
            print(f"{stack_arr} pinnar kvar i varje hög.")

            stack, move = player_input(stack_arr, stack_num)
            
            stack_arr[stack-1] -= move

            if sum(stack_arr) == 0:
                print(f"Du tog sista pinnen och vann!")
                break

            current_player = "computer"
        else:
            move_arr = best_move(stack_arr)
            stack_arr[move_arr[0]] -= move_arr[1]
            print(f"\nDatorn tar {move_arr[1]} pinnar från hög nummer {move_arr[0]+1}.")
            
            if sum(stack_arr) == 0:
                print(f"Datorn tog sista pinnen och vann!")
                break

            current_player = "human"


# Beskrivning: Denna funktion startas spelet samt tar in lite "inställningar", dvs. hur många pinnar spelaren önskar att spela med, hur många höägar de ska vara uppdelade i och om spelaren vill spela mot en dator eller mot en annan männsika. Pinnarna kommer även fördelas i högar med hjälp av stacks(). All input tas via input loopar. 
#
# Argument:
# void
#
# Return: 
# void
#
# Exempel: 
# Eftersom funktionen inte har några returns går det inte att skriva exempel.
#
# Datum: 2025-04-26
# Namn: Arvid Möller
def nim_game():
    print("Välkommen till Nim! Ditt mål är att ta den sista pinnen, du kan ta ett valfritt anatl pinnar ur varje hög.")

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
            if stack_num in range(2, 10) and stick_num/stack_num >= 1:
                break
            else:
                print("Ogiltigt antal högar, skriv ett tal mellan 2-10")
        except ValueError:
            print("Ogiltigt svar, skriv en siffra mellan 2-10")

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
        
    
# Starta spelet om det öppnas i terminalen
if __name__ == "__main__":
    nim_game()