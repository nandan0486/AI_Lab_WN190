
def depth_limited_search(node, goal, graph, limit, path):
    if node == goal:
        return path + [node]

    if limit == 0:
        return None

    for child in graph.get(node, []):
        if child not in path:
            result = depth_limited_search(
                child, goal, graph, limit - 1, path + [node]
            )

            if result is not None:
                return result

    return None


def iterative_deepening_search(initial, goal, graph, max_depth):
    for depth in range(max_depth + 1):
        print("Searching at depth limit:", depth)

        result = depth_limited_search(
            initial, goal, graph, depth, []
        )

        if result is not None:
            print("Goal found!")
            print("Solution Path:", " -> ".join(result))
            print("Depth:", len(result) - 1)
            return

    print("Goal not found within the maximum depth.")


# All 5 test cases
test_cases = [
    {
        "name": "Test Case 1: Goal at Depth 1",
        "initial": "A",
        "goal": "B",
        "max_depth": 3,
        "graph": {
            "A": ["B", "C"],
            "B": [],
            "C": []
        }
    },
    {
        "name": "Test Case 2: Goal at Depth 2",
        "initial": "A",
        "goal": "G",
        "max_depth": 3,
        "graph": {
            "A": ["B", "C"],
            "B": ["D", "E"],
            "C": ["F", "G"],
            "D": [],
            "E": [],
            "F": [],
            "G": []
        }
    },
    {
        "name": "Test Case 3: Goal Not Present",
        "initial": "A",
        "goal": "Z",
        "max_depth": 2,
        "graph": {
            "A": ["B", "C"],
            "B": ["D"],
            "C": ["E"],
            "D": [],
            "E": []
        }
    },
    {
        "name": "Test Case 4: Goal at Maximum Depth",
        "initial": "A",
        "goal": "G",
        "max_depth": 2,
        "graph": {
            "A": ["B", "C"],
            "B": ["D", "E"],
            "C": ["F", "G"],
            "D": [],
            "E": [],
            "F": [],
            "G": []
        }
    },
    {
        "name": "Test Case 5: Goal Not Present (Additional)",
        "initial": "A",
        "goal": "Z",
        "max_depth": 2,
        "graph": {
            "A": ["B", "C"],
            "B": ["D"],
            "C": ["E"],
            "D": [],
            "E": []
        }
    }
]


# Run all test cases automatically
for test in test_cases:
    print("\n" + "=" * 50)
    print(test["name"])
    print("=" * 50)

    print("Initial State:", test["initial"])
    print("Goal State:", test["goal"])
    print("Maximum Depth:", test["max_depth"])
    print("Search Tree:")

    for node, children in test["graph"].items():
        print(f"{node}: {', '.join(children) if children else '-'}")

    print("\nOutput:")
    iterative_deepening_search(
        test["initial"],
        test["goal"],
        test["graph"],
        test["max_depth"]
    )
