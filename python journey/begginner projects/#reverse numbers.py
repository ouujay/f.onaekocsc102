#reverse numbers
def reverse_order(list_of_numbers):
    reversed_numbers = list_of_numbers.copy()
    reversed_numbers.reverse()  # Reversing the order of numbers
    print("Reversed Numbers:", reversed_numbers)
    
    return reversed_numbers

list_of_numbers = [10, 2, 5, 3, 1]
print("Original Numbers:", list_of_numbers)
reversed_list = reverse_order(list_of_numbers)
