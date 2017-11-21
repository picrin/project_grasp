import sys

#fruits = sys.stdin.readline().rstrip().split()

fruits = ["orange", "apple", "grape", "banana", "poppy"]

def generate_perms(lista, result):
    if lista:
        for i, element in enumerate(lista):
            list_copy = lista[:]
            element = list_copy[i]
            del list_copy[i]
            generate_perms(list_copy, result + [element])
    else:
        print(result)

generate_perms(fruits, [])
