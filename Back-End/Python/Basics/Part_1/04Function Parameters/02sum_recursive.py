current_list = []
accumulated_list = []

def sum_recursive(current_number, accumulated_sum):
    # Base Case
    # Return the final state
    if current_number == 11:
        return accumulated_sum

    # Recursive case
    # Thread the state through the recursive call
    else:
        current_list.append(current_number)
        accumulated_list.append(accumulated_sum)
        return sum_recursive(current_number + 1, accumulated_sum + current_number)

print(sum_recursive(1, 0))
step_list = list(zip(current_list, accumulated_list))
print(f'Current List ==> {current_list}')
print(f'Accumulated List ==> {accumulated_list}')
print(f'Step List ==> {step_list}')
# >>> 55
# Current List ==> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Accumulated List ==> [0, 1, 3, 6, 10, 15, 21, 28, 36, 45]
# Step List ==> [(1, 0), (2, 1), (3, 3), (4, 6), (5, 10), (6, 15), (7, 21), (8, 28), (9, 36), (10, 45)]


