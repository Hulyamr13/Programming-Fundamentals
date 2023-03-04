from math import floor


def is_index_valid(index, elements_count):
    return 0 <= index < elements_count


def check_indexes_are_valid(index1, index2, elements_count):
    return (
        is_index_valid(index1, elements_count)
        and is_index_valid(index2, elements_count)
        and index1 != index2
    )


def add_penalty_elements(elements, n_moves):
    middle_index = floor(len(elements) / 2)
    elements.insert(middle_index, f"-{n_moves}a")
    elements.insert(middle_index, f"-{n_moves}a")


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