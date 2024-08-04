from collections import deque, defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_friend(self, person, friend):
        self.graph[person].append(friend)
        self.graph[friend].append(person)
    
    def find_common_friends(self, person1, person2):
        friends1 = set(self.graph[person1])
        friends2 = set(self.graph[person2])
        return friends1.intersection(friends2)
    
    def find_nth_connection(self, start, end):
        if start == end:
            return 0
        
        visited = {start}
        queue = deque([(start, 0)])  # (current_node, current_distance)
        
        while queue:
            current, distance = queue.popleft()
            for neighbor in self.graph[current]:
                if neighbor == end:
                    return distance + 1
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, distance + 1))
        
        return -1  # No connection found

# Example usage
g = Graph()
g.add_friend("Alice", "Bob")
g.add_friend("Bob", "Janice")
g.add_friend("Alice", "Charlie")

common_friends = g.find_common_friends("Alice", "Bob")
nth_connection = g.find_nth_connection("Alice", "Janice")

print("Common Friends:", common_friends)
print("Nth Connection (Alice to Janice):", nth_connection)
