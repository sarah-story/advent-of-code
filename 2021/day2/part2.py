def update_position(horizontal_position, depth, aim, command):
    match command.split(" "):
        case ["forward", amount]:
            horizontal_position += int(amount)
            depth += (aim * int(amount))
        case ["down", amount]:
            aim += int(amount)
        case ["up", amount]:
            aim -= int(amount)

    return horizontal_position, depth, aim


if __name__ == '__main__':
    horizontal_position = 0
    depth = 0
    aim = 0
    with open('input.txt') as file:
        for command in file:
            horizontal_position, depth, aim = update_position(
                horizontal_position, depth, aim, command.rstrip()
            )

    print(horizontal_position * depth)
