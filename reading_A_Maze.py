def read_maze(file_name):
    try:
        with open(file_name) as fh:
            maze = [[char for char in line.strip("\n")] for line in fh]
            num_of_columns = len(maze[0])
            for row in maze:
                if len(row) != num_of_columns:
                    print("The line is not rectangular")
                    raise SystemExit
        return maze
    except OSError:
        print("There is a prob")
        raise SystemExit


if __name__ == "__main__":
    maze = read_maze("modestmaze")
    for i in maze:
        print(i)

