from part1 import sliding_window_operation, compare_depths

if __name__ == '__main__':
    with open('input.txt') as file:
        depths = [int(line) for line in file]

    window_sums = sliding_window_operation(depths, 3, lambda x, y, z: x + y + z)
    print(sum(sliding_window_operation(window_sums, 2, compare_depths)))
