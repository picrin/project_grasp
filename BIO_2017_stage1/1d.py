import sys
#first_row = sys.stdin.readline()

#first_row = first_row.strip()

def compute_color(A, B):
    if A == B:
        return A
    if B < A:
        C = A
        A = B
        B = C
    if A == "B" and B == "R":
        return "G"
    elif A == "G" and B == "R":
        return "B"
    elif A == "B" and B == "G":
        return "R"

all_first_rows = []

possible_colours = ["R", "G", "B"]

def generate_all_first_rows(size):
    if size == 1:
        return possible_colours
    else:
        to_return = []
        for substring in generate_all_first_rows(size - 1):
            for suffix in possible_colours:
                to_return.append(substring + suffix)
        return to_return

def compute_last_row(first_row):
    current_row = first_row
    for j in range(len(current_row) - 1):
        next_row = []
        for i in range(len(current_row) - 1):
             letter = compute_color(current_row[i], current_row[i + 1])
             next_row.append(letter)
        current_row = "".join(next_row)
    return current_row

def check_property(n):
    possible_values = {}
    for row in generate_all_first_rows(n):
        last_letter = compute_last_row(row)
        first_last = row[0] + row[-1]
        if first_last not in possible_values:
            possible_values[first_last] = last_letter
        elif possible_values[first_last] == last_letter:
            pass
        else:
            return "Property doesn't hold for n = " + str(n)
    return "Property holds for n = " + str(n)

for n in range(1, 16):
    print(check_property(n))
