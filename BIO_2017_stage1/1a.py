import sys
first_row = sys.stdin.readline()

first_row = first_row.strip()

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

current_row = first_row
#print(current_row)
for j in range(len(current_row) - 1):
    next_row = []
    for i in range(len(current_row) - 1):
        letter = compute_color(current_row[i], current_row[i + 1])
        next_row.append(letter)
    current_row = "".join(next_row)
#    print(current_row)
print(current_row)
