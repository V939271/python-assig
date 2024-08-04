from collections import defaultdict, deque

# Function to perform topological sort
def topological_sort(graph, in_degree):
    queue = deque([node for node in in_degree if in_degree[node] == 0])
    sorted_order = []
    while queue:
        node = queue.popleft()
        sorted_order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    return sorted_order

def calculate_times(tasks, dependencies):
    # Initialize the graph
    graph = defaultdict(list)
    in_degree = {task: 0 for task in tasks}
    
    for pre, succ in dependencies:
        graph[pre].append(succ)
        in_degree[succ] += 1
    
    # Topological sort
    sorted_tasks = topological_sort(graph, in_degree)
    
    if len(sorted_tasks) != len(tasks):
        raise Exception("The graph has a cycle!")
    
    # Initialize times
    EFT = {task: 0 for task in tasks}
    LFT = {task: float('inf') for task in tasks}
    
    # Calculate EFT
    for task in sorted_tasks:
        for neighbor in graph[task]:
            EFT[neighbor] = max(EFT[neighbor], EFT[task] + tasks[task])
    
    # Assume the project completion time
    project_completion_time = max(EFT.values())
    
    # Calculate LFT
    for task in sorted_tasks[::-1]:
        if not graph[task]:  # If task has no outgoing edges
            LFT[task] = project_completion_time
        for neighbor in graph[task]:
            LFT[task] = min(LFT[task], LFT[neighbor] - tasks[neighbor])
    
    return EFT, LFT

# Example tasks and dependencies
tasks = {'A': 3, 'B': 2, 'C': 4, 'D': 1, 'E': 2}
dependencies = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'E')]

EFT, LFT = calculate_times(tasks, dependencies)

print("Earliest Finish Times:", EFT)
print("Latest Finish Times:", LFT)
