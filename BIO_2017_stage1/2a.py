from __future__ import print_function

valid_dot_no = list(range(1, 6 * 6 + 1))

clockwise = [-6, 1, 6 -1]

counter_clockwise = [-6, -1, 6, 1]

check_square_up = clockwise
check_square_right = [1, 6, -1, -6]
check_square_down = [-6, 1, 6, -1]
check_square_left = [-1, 6, 1, -6]

all_directions = [check_square_up, check_square_right, check_square_down, check_square_left]

edges = {}

def candidate_squares(dot, order):
    current_dot = dot
    candidate_edges = []
    for offset in order:
        next_dot = current_dot + offset
        candidate_edges.append((current_dot, next_dot))
        current_dot = next_dot
    return candidate_edges

def candidate_moves(dot, order):
    current_dot = dot
    candidate_edges = []
    for offset in order:
        candidate_edges.append([current_dot, current_dot + offset])
    return candidate_edges

def check_square(dot_no, direction):
    count = 0
    for edge in candidate_squares(dot_no, direction):
        if check_edge(*edge):
            count += 1
    return count == 4

def return_squares():
    squares = []
    for i in range(1, 31):
        squares.append(check_square(i, check_square_right))
    return squares


def print_squares():
    for i, square in enumerate(squares_taken):
        if (i + 1) % 6 == 0:
            print("")
        else:
	    print(square, end="")
    print()

def up(dot_no):
    candidate = dot_no - 6
    if candidate in valid_dot_no:
        return candidate

def down(dot_no):
    candidate = dot_no + 6
    if candidate in valid_dot_no:
        return candidate

def left(dot_no):
    if (dot_no - 1) % 6 - 1 >= 0:
        return dot_no - 1

def right(dot_no):
    if (dot_no - 1) % 6 + 1 < 6:
        return dot_no + 1

def list_adjacent(dot_no):
    valid_adjacent = [func(dot_no) for func in [up, down, left, right]]
    valid_adjacent = [i for i in valid_adjacent if i is not None]
    return valid_adjacent

def check_edge(dot1, dot2):
    if dot2 not in list_adjacent(dot1) or tuple(sorted([dot1, dot2])) not in edges:
        return False
    else:
        return True

def fill_edge(dot1, dot2):
    if dot2 not in list_adjacent(dot1) or tuple(sorted((dot1, dot2))) in edges:
        return False
    else:
        sorted_edges = tuple(sorted([dot1, dot2]))
        edges[sorted_edges] = True
        return True

squares_taken = [0 for i in return_squares()]

def fill_edge_check_square(dot1, dot2, player):
    squares_before = return_squares()
    fill_edge(dot1, dot2)
    squares_after = return_squares()
    for i, pair in enumerate(zip(squares_before, squares_after)):
        if pair[0] != pair[1]:
            squares_taken[i] = player

def main_function(p1, p2, m1, m2, d1, d2, t, player):
    print_squares()
    if 0 not in squares_taken:
        print("All squares are taken. Game Over.")
        return
    if t == 0:
        print("End of simulation. Max t reached")
        return
    if player == 1:
        next_player = 2
    else:
        next_player = 1
    moves = candidate_moves(p1, d1)
    for move in moves:
        if not check_edge(*move):
            fill_edge_check_square(move[0], move[1], next_player)
            next_position = (p1 + m1 - 1) % 36 + 1
            return main_function(p2, next_position, m2, m1, d2, d1, t - 1, next_player)
    return main_function(p1 + 1, p2, m1, m2, d1, d2, t - 1, next_player)

main_function(4, 10, 14, 23, clockwise, counter_clockwise, 47, 1)
#print(1, list_adjacent(1))
#print(4, list_adjacent(4))
#print(12, list_adjacent(12))
#print(30, list_adjacent(30))
#print(31, list_adjacent(31))
#print(36, list_adjacent(36))
#print(21, list_adjacent(21))
#
#print(check_edge(12, 13))
#print(fill_edge(10, 11))
#print(check_edge(10, 11))
#print(edges)
#fill_edge_check_square(1, 2, 2)
#print(edges)
#fill_edge_check_square(2, 8, 2)
#print(edges)
#fill_edge_check_square(8, 7, 2)
#print(edges)
#fill_edge_check_square(7, 1, 2)
#print(edges)

#print(squares_taken)

#print(fill_edge_check_square(8, 14, 2))
#print(edges)
#print(fill_edge_check_square(14, 13, 2))
#print(edges)
#print(fill_edge_check_square(13, 7, 2))
#print(edges)

#print_squares()

#print(squares_taken)

#print_squares()

#print(fill_edge(19, 13, 2))
#print(check_edge(13, 14))

#print(return_squares())

#main_loop(4, 10, 14, 23)


#print(check_square(1, check_square_down))
#print(check_square(1, check_square_up))
#print(check_square(1, check_square_left))
#print(check_square(1, check_square_right))

#print(return_squares())
