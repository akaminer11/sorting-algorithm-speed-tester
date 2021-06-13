import random
def generate_random_list(num):
    l = []
    for i in range(num):
        l.append(random.randint(0, 1000))
    return l

# literally just a utility function