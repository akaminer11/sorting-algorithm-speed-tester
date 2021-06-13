import gen_random, bubble_sort, insertion_sort, merge_sort, quick_sort, selection_sort
import time, sys

args = sys.argv

dictionary = {
"bsort" : bubble_sort.bubble_sort, 
"isort" : insertion_sort.insertion_sort,
"msort" : merge_sort.merge_sort,
"qsort" : quick_sort.quick_sort,
"ssort" : selection_sort.select_sort
}

def help():
    text = "Sorts a random list of user provided length using user chosen sorting algorithm.\n\nSorting types:\n\nqsort: quick sort\nisort: insertion sort\nmsort: merge sort\nbsort: bubble sort\nssort: selection sort\n\nIf list length is over 100, it will not be shown. Use -f to override.\n"
    print(text)


force = False

if len(args) > 1:
    if args[1] == "-h" or args[1] == "--help":
        help()
        sys.exit()
    elif args[1] == "-f":
        force = True
    else:
        print("Invalid argument(s)")
        sys.exit()

sort_type = input("Please select a sorting type. To find sorting types and optional arguments, use -h or --help\n")
if sort_type not in dictionary.keys():
    print("Incorrect sorting type. Please try again.")
    sys.exit()

length = int(input("Select list length\n"))

l = gen_random.generate_random_list(int(length))

print_list = False
if length < 100 or force:
    print_list = True

if print_list:
    print(str(l) + "\n\n\n")

t1 = time.time()
if sort_type != "qsort":
    t1 = time.time()
    l = dictionary[sort_type](l)
    t2 = time.time()
else:
    t1 = time.time()
    dictionary[sort_type](l, 0, len(l)-1)
    t2 = time.time() 

if print_list:
    print(str(l))

print(f"\nTime: {t2-t1} seconds.")