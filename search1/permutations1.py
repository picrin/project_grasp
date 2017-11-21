fruits = ["orange", "apple", "banana"]

def permutations(partial_perm, elements_left):
    if len(elements_left) == 0:
        print(partial_perm)
    else:
        for i in range(len(elements_left)):
            new_partial_perm = partial_perm + [elements_left[i]]
            new_elements_left = elements_left[0:i] + elements_left[i+1:]
            permutations(new_partial_perm, new_elements_left)

permutations([], fruits)
