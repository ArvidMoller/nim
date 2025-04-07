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
    print("bst move")
    stack = 0
    while stack < len(stack_arr):
        for move in range(1,4):
            print("in for loop")
            tmp_arr = stack_arr.copy()
            print(stack_arr)
            if tmp_arr[stack] - move >= 0:
                tmp_arr[stack] -= move 
                if xor_sum(tmp_arr) == 0:
                    print("bst move found")
                    return stack, move
                possible_move = [stack, move]
        stack+=1
    
    return possible_move
    


# print(best_move([0, 0, 0, 0]))

print(xor_sum([1, 0, 1]))