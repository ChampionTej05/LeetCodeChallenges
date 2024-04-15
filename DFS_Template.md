```python
def dfs(node, state, result):
    # Base Case: check if the current node/state should terminate the search
    if should_terminate(node, state):
        process_result(node, state, result)
        return

    # Recursive Case: explore adjacent nodes/states
    for next_node in get_adjacent_nodes(node, state):
        if is_valid(next_node, state):
            # Modify state if necessary
            new_state = update_state(state, next_node)
            
            # Recursive DFS call
            dfs(next_node, new_state, result)
            
            # Backtrack if necessary (undo state modification)
            undo_state_modification(state, next_node)

# Usage example
result = []
initial_state = ...  # Depends on the problem
initial_node = ...   # Starting point
dfs(initial_node, initial_state, result)
```

# Key Components of the DFS Template
**Node/State**: Represents the current position or condition in your search space.
**Base Case**: The condition under which the search should stop. This could be finding a solution, reaching a dead end, or satisfying a certain constraint.
**Process Result**: If the base case is met, process the result as needed (e.g., add to a list of solutions, print output).
**Recursive Case**: Explore adjacent nodes or states. This could involve iterating over a set of choices, adjacent graph nodes, etc.
**Validity Check**: Before making a recursive call, check if the next node/state is valid under the problem's constraints.
**State Update and Backtracking**: Modify the state for the next recursive call. After the call, undo the modification (backtrack) to restore the state for exploring other paths.

# Notes
Adaptability: This template is highly adaptable. Depending on the problem, you might not need all the components (like explicit backtracking).
Graphs and Trees: For graph problems, you might need to keep track of visited nodes to avoid cycles.
Combinatorial Problems: In problems like permutations, combinations, or subsets, DFS explores different choices at each step.
Puzzle Solving: DFS can be used in puzzles (like Sudoku or crossword puzzles) to try different configurations.

# Example Usage
The template can be adapted for specific problems like path finding in a maze, solving Sudoku, finding combinations or permutations of elements, traversing trees or graphs, etc. The key is to identify how node, state, should_terminate, get_adjacent_nodes, and is_valid apply to your specific problem.