# There are n bins each with volume v. There are k objects, of varying volume. Find the minimum number of bins which can contain all the objects.

# Example input v = 10, objects volume = 2, 5, 4, 7, 1, 3, 8

# example solution = [[7, 3], [8, 2], [5, 4, 1]] <- this is guaranteed to be the optimal solution, as we managed to fully pack all 3 bins.

# Reference: SR1 in Garey and Johnson

finished = False

solution = None

def validate_partial_solution(next_solution, data, v):
    bins_to_weight = {}
    for bin_no, data in zip(next_solution, data):
        bins_to_weight[bin_no] = bins_to_weight.get(bin_no, 0) + data
    for _, value in bins_to_weight.items():
        if value > v:
            return False
    return True

def backtrack(partial_solution, data, number_of_bins, v):
    global finished
    global solution
    if len(partial_solution) == len(data):
        finished = True
        solution = partial_solution
    choice_space = range(1, number_of_bins + 1)
    for possible_choice in choice_space:
        next_solution = partial_solution + [possible_choice]
        if validate_partial_solution(next_solution, data, v) and not finished:
            backtrack(next_solution, data, number_of_bins, v)

def optimal_packing(v, data):
    global finished
    global solution
    finished = False
    solution = None
    for number_of_bins in range(1, len(data) + 1):
        backtrack([], data, number_of_bins, v)
    human_friendly_solution = {}
    for s, d in zip(solution, data):
        human_friendly_solution[s] = human_friendly_solution.get(s, []) + [d]
    human_friendly_solution = [sol for _, sol in human_friendly_solution.items()]
    return human_friendly_solution

def heuristic_packing(v, data):
    data2 = sorted(data, reverse=True)
    best_fit_decreasing = []
    for item in data2:
        min_i = 0
        minimal = v
        placed = False
        for i, b in enumerate(best_fit_decreasing):
            value = sum(b) + item
            left = v - value
            if value <= v and left <= minimal:
                placed = True
                minimal = left
                min_i = i
        if placed:
            best_fit_decreasing[min_i].append(item)
        else:
            best_fit_decreasing.append([item])
    return best_fit_decreasing
import random

def find_non_trivial(v, k):
    while True:
        data = [random.randint(1, v-1) for i in range(k)]
        data = sorted(data, reverse=True)
        print(data)
        if len(optimal_packing(v, data)) != len(heuristic_packing(v, data)):
            break
    return(data)

v=7
objects = [3, 3, 2, 2, 2, 2]
print(optimal_packing(v, objects))
print(heuristic_packing(v, objects))
