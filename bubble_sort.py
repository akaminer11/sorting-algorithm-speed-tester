import gen_random, sys, time

def bubble_sort(list):
    while True:
        i = 0
        counter = 0
        while i < len(list)-1:
            if list[i] > list[i+1]:
                swap(i, i+1, list)
                i += 1
                counter += 1
            else:
                i += 1
        if counter == 0:
            break
    return list

def swap(a, b, list):
    list[a], list[b] = list[b], list[a]





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
    s = bubble_sort(l)
    t2 = time.time()
    print("time: " + str(t2-t1) + " seconds")  # I realize that this is painfully ugly code down here but it isn't the part that matters
    if len(l) < 100 or arg == "-f":
        print("Sorted: \n" + str(s) + "\n")