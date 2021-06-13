import gen_random, time, sys

def quick_sort(list, low, high):
    if  high > low:
        pi = partition(list, low, high)

        quick_sort(list, low, pi - 1)
        quick_sort(list, pi + 1, high)


def partition(list, low, high):
    pivot = list[high]
    small_element_index = low - 1

    for x in range(low, high):
        if list[x] < pivot:
            small_element_index += 1
            swap(list, small_element_index, x)
    
    swap(list, small_element_index + 1, high)
    return small_element_index + 1


# utility function to swap items in a list
def swap(list, a, b):
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
    quick_sort(l, 0, len(l)-1)
    t2 = time.time()
    print("time: " + str(t2-t1) + " seconds")  # I realize that this is painfully ugly code down here but it isn't the part that matters
    if len(l) < 100 or arg == "-f":
        print("Sorted: \n" + str(l) + "\n")