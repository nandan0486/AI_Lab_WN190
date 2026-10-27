
def vacuum_agent(location, status_A, status_B):
    if location == "A" and status_A == "Dirty":
        return "SUCK"
    elif location == "B" and status_B == "Dirty":
        return "SUCK"
    elif status_A == "Dirty":
        return "LEFT"
    elif status_B == "Dirty":
        return "RIGHT"
    else:
        return "NO-OP"


def vacuum_simulation(location, status_A, status_B):
    actions = []

    while True:
        action = vacuum_agent(location, status_A, status_B)

        if action == "NO-OP":
            actions.append("NO-OP")
            print("Action:", action)
            break

        actions.append(action)

        if action == "SUCK":
            if location == "A":
                status_A = "Clean"
            else:
                status_B = "Clean"

        elif action == "LEFT":
            location = "A"

        elif action == "RIGHT":
            location = "B"

        print("Action:", action)
        print("Location:", location)
        print("Room A:", status_A)
        print("Room B:", status_B)
        print()

    print("Final Environment State:")
    print("Location:", location)
    print("Room A:", status_A)
    print("Room B:", status_B)
    print("Actions Performed:", " -> ".join(actions))


# All 7 test cases
test_cases = [
    {
        "name": "Test Case 1: Both Rooms Dirty, Starting in A",
        "location": "A",
        "A": "Dirty",
        "B": "Dirty"
    },
    {
        "name": "Test Case 2: A Clean, B Dirty, Starting in A",
        "location": "A",
        "A": "Clean",
        "B": "Dirty"
    },
    {
        "name": "Test Case 3: Both Rooms Clean, Starting in B",
        "location": "B",
        "A": "Clean",
        "B": "Clean"
    },
    {
        "name": "Test Case 4: Both Rooms Dirty, Starting in B",
        "location": "B",
        "A": "Dirty",
        "B": "Dirty"
    },
    {
        "name": "Test Case 5: A Dirty, B Clean, Starting in B",
        "location": "B",
        "A": "Dirty",
        "B": "Clean"
    },
    {
        "name": "Test Case 6: A Clean, B Dirty, Starting in B",
        "location": "B",
        "A": "Clean",
        "B": "Dirty"
    },
    {
        "name": "Test Case 7: Both Rooms Clean, Starting in A",
        "location": "A",
        "A": "Clean",
        "B": "Clean"
    }
]


# Execute all test cases
for test in test_cases:
    print("\n" + "=" * 50)
    print(test["name"])
    print("=" * 50)

    print("Initial Location:", test["location"])
    print("Initial Room A:", test["A"])
    print("Initial Room B:", test["B"])
    print("\nExecution:")

    vacuum_simulation(
        test["location"],
        test["A"],
        test["B"]
    )
