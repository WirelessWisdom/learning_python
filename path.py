custom_map = [
    ["o", None, None, None, None],
    [None, None, "o", None, None],
    [None, "o", None, None, None],
    [None, None, None, None, None],
    [None, None, None, None, None]
]

start = (4, 0)
finish = (0, 4)


def pathfinder(starting_point: tuple[int, int], finish_point: tuple[int, int], field: list[list]):
    points_list = [starting_point]
    moves_list = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    field[starting_point[0]][starting_point[1]] = 0

    while points_list:
        point = points_list.pop(0)
        point_value = field[point[0]][point[1]]
        if point == finish_point:
            return path_coordinates(field, finish_point)

        for move in moves_list:
            x, y = point[0] + move[0], point[1] + move[1]

            if x >= len(field) or x < 0 or y < 0 or y >= len(field[1]):
                continue
            if field[x][y] == "o" or field[x][y] is not None:
                continue

            field[x][y] = point_value + 1
            points_list.append((x, y))

    return "No way out"


def path_coordinates(field, start_point: tuple[int, int]):
    points_list = [start_point]
    result_list = [start_point]
    moves_list = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    while points_list:
        point = points_list.pop(0)
        point_value = field[point[0]][point[1]]
        if point_value == 0:
            return result_list[::-1]

        for move in moves_list:
            x, y = point[0] + move[0], point[1] + move[1]

            if x >= len(field) or x < 0 or y < 0 or y >= len(field[1]):
                continue
            if field[x][y] == point_value - 1:
                points_list.append((x, y))
                result_list.append((x, y))
                break
    return "No way out"


def print_path(field, path):
    for x, y in path:
        field[x][y] = "*"
    for line in field:
        print(line)


#pathfinder(start, finish, custom_map)
print_path(custom_map, pathfinder(start, finish, custom_map))
