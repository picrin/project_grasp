from __future__ import print_function
# first small task -- 
def point_above(point1):
    if point1 > 6:
        return point1 - 6
    else: 
        return 0

def point_below(point1):
    if point1 < 31:
        return point1 + 6
    else: 
        return 0

def point_right(point1):
    if point1 % 6 != 0:
        return point1 + 1
    else: 
        return 0

def point_left(point1):
    if point1 % 6 != 1:
        return point1 - 1
    else: 
        return 0

clockwise = [point_above, point_right, point_below, point_left]
anticlockwise = [point_above, point_left, point_below, point_right]

taken_edges = {}
# taken_squares = [0]*25
squares = {}
def populate_squares():
    for point in range(1, 31):
        if not point % 6 == 0:
            squares[point] = 0
populate_squares()

def neighbourhood(point1, direction):
    result = []
    for function in direction:
        point_or_zero = function(point1)
        if point_or_zero != 0:
            result.append(point_or_zero)
    return result

def is_edge_taken(edge):
    return edge in taken_edges

def take_edge(edge):
    # Need to swap edges to be in correct order
    (a,b) = edge
    if not is_edge_taken(edge):
        taken_edges[(a,b)] = True
        taken_edges[(b,a)] = True
        return True
    return False

def is_square_taken(top_left_point):
    right_point = point_right(top_left_point)
    below_point = point_below(top_left_point)
    top_edge = is_edge_taken((top_left_point, right_point))
    left_edge = is_edge_taken((top_left_point, below_point)) 
    bottom_edge = is_edge_taken((below_point, point_right(below_point)))
    right_edge = is_edge_taken((right_point, point_below(right_point)))
    if top_edge and left_edge and bottom_edge and right_edge:
        return True
    return False

def print_squares():
    for point in range(1, 31):
        if point % 6 == 0:
            print("")
        else:
            square = squares[point]
            if square == 1:
    	        print("X", end="")
            elif square == 2:
                print("O", end="")
            else:
                print("*", end="")

    print("")

print_squares()
def main(p1, p2, m1, m2, t, d1, d2, player_number):
    if player_number == 1:
        next_player = 2
    else:
        next_player = 1
    
    print_squares()
    if t == 0:
        print("Reached simulation depth")
        return
    if not [0 for value in squares.values() if value == 0]:
        print("Game over, no more squares!")
        return
    possible_edges = []
    for second_point in neighbourhood(p1, d1):
        possible_edges.append((p1, second_point))
    edge_taken = False

    for possible_edge in possible_edges:
        if not is_edge_taken(possible_edge):
            take_edge(possible_edge)
            edge_taken = True
            break
    
    if edge_taken:
        new_p1 = (p1 + m1 - 1) % 36
        membership_changed = False
        # check membership
        for top_left in squares:
            previous_member = squares[top_left]
            is_taken = is_square_taken(top_left)
            if previous_member == 0 and is_taken:
                membership_changed = True
                squares[top_left] = player_number
        if membership_changed:
            return main(new_p1, p2, m1, m2, t - 1, d1, d2, player_number)
        else:
            return main(p2, new_p1, m2, m1, t - 1, d2, d1, next_player)
    else:
        new_p1 = (p1 + 1 - 1) % 36 + 1
        return main(new_p1, p2, m1, m2, t, d1, d2, player_number)

main(4, 10, 14, 23, 47, clockwise, anticlockwise, 1)
