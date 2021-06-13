import gen_random, time, sys

def merge(L, R):
    merged = []
    left_index, right_index, merge_index = 0, 0, 0
    
    # go through the arrays and check for anything left over
    while left_index < len(L) and right_index < len(R):
        if L[left_index] > R[right_index]:
            merged.append(R[right_index])
            right_index += 1
        else:
            merged.append(L[left_index])
            left_index += 1

    # check for anything left over
    while left_index < len(L):
        merged.append(L[left_index])
        left_index += 1

    while right_index < len(R):
        merged.append(R[right_index])
        right_index += 1

    # return the new array
    return merged

def merge_sort(list):
    if len(list) == 1:
        return list

    mid = len(list) // 2

    L = list[:mid]
    R = list[mid:]

    L = merge_sort(L)
    R = merge_sort(R)

    return merge(L, R)
        





# basic testing functionality
if __name__ == "__main__":
    if (len(sys.argv) > 1):
        arg = sys.argv[1]
    else:
        arg = "nope"
    num = int(input("\nHow big do you want the list to be? If the number is 100 or over, the list will not be shown. To override, restart the program and use -f\n"))
    l = gen_random.generate_random_list(num)
    if len(l) < 100 or arg == "-f":
        print("\nOriginal: \n" + str(l) + "\n")
    t1 = time.time()
    s = merge_sort(l)
    t2 = time.time()
    print("time: " + str(t2-t1) + " seconds")  # I realize that this is painfully ugly code down here but it isn't the part that matters
    if len(l) < 100 or arg == "-f":
        print("Sorted: \n" + str(s) + "\n")