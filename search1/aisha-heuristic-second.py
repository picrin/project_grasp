# Bin size
v = 10
# Objects
numbers = [8, 7, 5, 1, 2, 3, 4]

# Sort into descending order
numbers.sort(reverse=True)
# Our packing
packing = []

# While we have objects to pack
while numbers:
    # Take the biggest one off the list
    biggest = numbers.pop(0)
    # Make a new bin
    new_bin = [biggest]
    new_item_added = True
    # Keep doing this loop until we can't add more things
    while new_item_added:
        # We started a new loop, so we haven't added anything
        new_item_added = False
        # Go through the remaining objects
        for index, number in enumerate(numbers):
            # If it fits into the next bin
            if number + sum(new_bin) <= v:
                # Put it in the new bin, remove it from our list, and make a
                # note that we have added a new object
                new_bin.append(number)
                numbers.pop(index)
                new_item_added = True
    # Put our new bin into our list of bins
    packing.append(new_bin)
# Lastly, print out our packing
print(packing)
