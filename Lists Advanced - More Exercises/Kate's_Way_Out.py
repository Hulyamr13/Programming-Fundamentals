nums = int(input())
kaze = []
for i in range(nums):
    kaze.append(input())

maze = []
moves = 0

for line in kaze:
    maze.append(list(''.join(line)))

height = len(maze)
width = len(maze[0])


def find_position(maze):
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if maze[y][x] == 'k':
                k = [y, x]
                if 0 <= y + 1 < height:
                    down = [y + 1, x]
                else:
                    down = False
                if 0 <= x - 1 < width:
                    left = [y, x - 1]
                else:
                    left = False
                if 0 <= x + 1 < width:
                    right = [y, x + 1]
                else:
                    right = False
                if 0 <= y - 1 < height:
                    up = [y - 1, x]
                else:
                    up = False

    return [k, down, left, right, up]


while True:
    k, down, left, right, up = find_position(maze)
    if left and maze[left[0]][left[1]] == ' ':
        maze[k[0]][k[1]] = '#'
        maze[left[0]][left[1]] = 'k'
        moves += 1
    elif right and maze[right[0]][right[1]] == ' ':
        maze[k[0]][k[1]] = '#'
        maze[right[0]][right[1]] = 'k'
        moves += 1
    elif down and maze[down[0]][down[1]] == ' ':
        maze[k[0]][k[1]] = '#'
        maze[down[0]][down[1]] = 'k'
        moves += 1
    elif up and maze[up[0]][up[1]] == ' ':
        maze[k[0]][k[1]] = '#'
        maze[up[0]][up[1]] = 'k'
        moves += 1
    elif k[0] == height - 1 or k[0] == 0 or k[1] == width - 1 or k[1] == 0:
        moves += 1
        print(f'Kate got out in {moves} moves')
        break
    else:
        print('Kate cannot get out')
        break