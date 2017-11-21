numbers = [3, 3, 2, 2, 2, 2]
numbers.sort(reverse=True)

new_numbers = [numbers]

v = 7

packing = [[]]
used = [False] * len(numbers)

packing_index = 0
while not all(used):
    current_bin = packing[packing_index]
    packed = False
    for i, number in enumerate(numbers):
        if number + sum(current_bin) <= v and not used[i]:
            current_bin.append(number)
            packed = True
            used[i] = True
    if not packed:
        packing_index += 1
        packing.append([])

print(packing)
