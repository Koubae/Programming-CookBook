
current_number = 1
accumulated_sum = 0


def sum_recursive():
    global current_number
    global accumulated_sum
    # Base Case
    if current_number == 11:
        return accumulated_sum
    # Recursive Case
    else:
        accumulated_sum = accumulated_sum + current_number
        current_number = current_number + 1
        return sum_recursive()

print(sum_recursive())
# >>> 55