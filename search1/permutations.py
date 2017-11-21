fruits = ["banana", "apple", "strawberry"]

def extend_solution(partial_solution, remaining_options):
    if len(remaining_options) == 0:
        print(partial_solution)
    else:
        for i, remaining_option in enumerate(remaining_options):
            extended_solution = partial_solution + [remaining_option]
            # exclude remaining_option from remaining_options and call it other_options
            extend_solution(extended_solution, remaining_options[:i] + remaining_options[i+1:])

extend_solution([], fruits)
