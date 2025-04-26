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
# best_move([1, 2, 3, 4]) => [3, 3]
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
                    print("bst move found")
                    return stack, move
                elif tmp_arr[stack] - move >= 0:
                    possible_move = [stack, move]
        stack+=1
    
    return possible_move
    


print(best_move([6, 3, 9]))