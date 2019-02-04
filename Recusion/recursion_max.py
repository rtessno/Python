def max(numbers, largest_so_far=None):
    if not numbers:
        return largest_so_far
    elif not largest_so_far or numbers[0] > largest_so_far:
        return max(numbers[1:], numbers[0])
    else:
        return max(numbers[1:], largest_so_far)

print(max([4403, 8593, 3306] ))