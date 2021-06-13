import gen_random, time, sys

def find_min_index(i, list):
    min_indx = i
    for j in range(i+1, len(list)):
        if list[min_indx] > list[j]:
            min_indx = j
    return min_indx

def insertion_sort(list):
    for step in range(1, len(list)): 
        key = list[step] 
        j = step - 1

        while j >=0 and list[j] > key: # compare the key and the element before it until a smaller element is found
            list[j+1] = list[j]
            j -= 1

        list[j+1] = key # put key just after the element smaller than it

    return list




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
    s = insertion_sort(l)
    t2 = time.time()
    print("time: " + str(t2-t1) + " seconds")  # I realize that this is painfully ugly code down here but it isn't the part that matters
    if len(l) < 100 or arg == "-f":
        print("Sorted: \n" + str(s) + "\n")