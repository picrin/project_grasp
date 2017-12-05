
def count_minimum_strokes_inner(strokes_allowed, current_elements, count, distance):
    next_elements = set({})
    if distance in current_elements:
        return count
    if not current_elements:
        return -1
    for element in current_elements:
        for stroke in strokes_allowed:
            next_element = element + stroke
            if next_element <= distance:
                next_elements.add(next_element)
    return count_minimum_strokes_inner(strokes_allowed, next_elements, count + 1, distance)


def count_minimum_strokes(strokes_allowed, distance):
    return count_minimum_strokes_inner(strokes_allowed, set([0]), 0, distance)

def count_minimum_strokes_loop(strokes_allowed, distance):
    current_elements = set([0])
    count = 0
    result = -1
    while current_elements:
        next_elements = set({})
        if distance in current_elements:
            break
        if not current_elements:
            break
        for element in current_elements:
            for stroke in strokes_allowed:
                next_element = element + stroke
                if next_element <= distance:
                    next_elements.add(next_element)
        count += 1
        current_elements = next_elements
    return count

print(count_minimum_strokes([28, 56, 47], 140))
print(count_minimum_strokes([28, 56, 47], 140))
