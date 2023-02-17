#!/usr/bin/python

# Function to find and order list of numbers
def buscar(input:list) -> list:
    numbers = [5,7,9]
    order_numbers = []
    output = []    

    for n in numbers:
        if n in input and n not in order_numbers:
            order_numbers.append(n)

    if order_numbers:
        output = sorted(order_numbers)    

    return output


def main():
    search_list_1 = [1,7,13,22,5,12,30]
    search_list_2 = [7,3,9,9,12,40,5]

    print('Lista 1:',search_list_1)
    print('Lista 2:',search_list_2)
    input_list = list(map(int,input("Informe uma nova lista de números separados por espaço: ").split()))    

    list_1 = buscar(search_list_1)
    list_2 = buscar(search_list_2)
    list_3 = buscar(input_list)

    print('Números encontrados lista 1:',list_1)
    print('Números encontrados lista 2:',list_2)
    print('Números encontrados lista 3:',list_3)    


main()
