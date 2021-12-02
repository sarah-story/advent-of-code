def update_position(horizontal_position, depth, command):
    match command.split(" "):
        case ["forward", amount]:
            horizontal_position += int(amount)
        case ["down", amount]:
            depth += int(amount)
        case ["up", amount]:
            depth -= int(amount)

    return horizontal_position, depth


if __name__ == '__main__':
    horizontal_position = 0
    depth = 0
    with open('input.txt') as file:
        for command in file:
            horizontal_position, depth = update_position(horizontal_position, depth, command.rstrip())

    print(horizontal_position * depth)

