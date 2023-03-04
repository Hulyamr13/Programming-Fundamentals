from math import floor

is_index_valid = lambda index, elements_count: 0 <= index < elements_count


check_indexes_are_valid = lambda index1, index2, elements_count: (
        is_index_valid(index1, elements_count)
        and is_index_valid(index2, elements_count)
        and index1 != index2
)


add_penalty_elements = lambda elements, n_moves: (
        elements.insert(floor(len(elements) / 2), f"-{n_moves}a"),
        elements.insert(floor(len(elements) / 2), f"-{n_moves}a")
)


def play_game():
    elements = input().split()
    n_moves = 0

    while True:
        command = input()
        if command == "end":
            break

        if len(elements) < 2:
            continue

        n_moves += 1
        index1, index2 = map(int, command.split())

        if not check_indexes_are_valid(index1, index2, len(elements)):
            add_penalty_elements(elements, n_moves)
            print("Invalid input! Adding additional elements to the board")
            continue

        if elements[index1] == elements[index2]:
            print(f"Congrats! You have found matching elements - {elements[index1]}!")
            if index2 > index1:
                index2 -= 1
            elements.pop(index1)
            elements.pop(index2)
        else:
            print("Try again!")

        if len(elements) < 2:
            print(f"You have won in {n_moves} turns!")
            break

    if len(elements) >= 2:
        print("Sorry you lose :(")
        print(*elements)

play_game()