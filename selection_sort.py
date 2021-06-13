import gen_random, time, sys

def find_min_index(i, list):
    min_indx = i
    for j in range(i+1, len(list)):
        if list[min_indx] > list[j]:
            min_indx = j
    return min_indx

def select_sort(list):
    for i in range(len(list)):
        min_indx = find_min_index(i, list) # find the index of the least element in the list

        list[i], list[min_indx] = list[min_indx], list[i] # swap the two

    return list # return the new list
    





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
    s = select_sort(l)
    t2 = time.time()
    print("time: " + str(t2-t1) + " seconds")  # I realize that this is painfully ugly code down here but it isn't the part that matters
    if len(l) < 100 or arg == "-f":
        print("Sorted: \n" + str(s) + "\n")