import heapq

# Goal state
GOAL = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)   # 0 represents blank (_)


# Display the puzzle
def display(state):
    for i in range(0, 9, 3):
        row = []
        for x in state[i:i+3]:
            if x == 0:
                row.append("_")
            else:
                row.append(str(x))
        print(" ".join(row))
    print()


# Manhattan Distance heuristic
def manhattan_distance(state):
    distance = 0

    for i, tile in enumerate(state):
        if tile != 0:
            # Current position
            current_row = i // 3
            current_col = i % 3

            # Goal position
            goal_index = GOAL.index(tile)
            goal_row = goal_index // 3
            goal_col = goal_index % 3

            distance += abs(current_row - goal_row)
            distance += abs(current_col - goal_col)

    return distance


# Generate successor states
def get_successors(state):
    successors = []

    blank = state.index(0)
    row = blank // 3
    col = blank % 3

    moves = [
        ("UP", row - 1, col),
        ("DOWN", row + 1, col),
        ("LEFT", row, col - 1),
        ("RIGHT", row, col + 1)
    ]

    for action, new_row, new_col in moves:

        # Check whether move is legal
        if 0 <= new_row < 3 and 0 <= new_col < 3:

            new_blank = new_row * 3 + new_col

            new_state = list(state)

            # Swap blank with the tile
            new_state[blank], new_state[new_blank] = \
                new_state[new_blank], new_state[blank]

            successors.append((tuple(new_state), action))

    return successors


# A* Search
def a_star(start):
    # Priority queue
    # (f, g, state, path)
    frontier = []

    h = manhattan_distance(start)

    heapq.heappush(frontier, (h, 0, start, []))

    explored = set()

    while frontier:

        f, g, state, path = heapq.heappop(frontier)

        # Goal test
        if state == GOAL:
            return path, g

        if state in explored:
            continue

        explored.add(state)

        # Generate successors
        for new_state, action in get_successors(state):

            if new_state not in explored:

                new_g = g + 1
                new_h = manhattan_distance(new_state)
                new_f = new_g + new_h

                new_path = path + [(action, new_state)]

                heapq.heappush(
                    frontier,
                    (new_f, new_g, new_state, new_path)
                )

    return None, None


# Read input
print("Enter the initial 8-puzzle configuration")
print("Use _ for the blank space.")

values = []

for i in range(3):
    row = input().split()

    for value in row:
        if value == "_":
            values.append(0)
        else:
            values.append(int(value))

start = tuple(values)


# Display initial state
print("\nInitial State:")
display(start)


# Check if already solved
if start == GOAL:
    print("Goal State Reached")
    print("Solution Cost = 0")

else:
    # Run A*
    solution, cost = a_star(start)

    if solution is None:
        print("No solution exists.")

    else:
        # Display solution
        for i, (action, state) in enumerate(solution, start=1):
            print("Move", i, ":", action)
            display(state)

        print("Goal State Reached")
        print("Solution Cost =", cost)
