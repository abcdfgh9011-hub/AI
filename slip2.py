#Q1

from collections import deque
def water_jug(cap1, cap2, target):
    q = deque([(0, 0)])
    visited = set()
    while q:
        x, y = q.popleft()
        if (x, y) in visited:
            continue
        visited.add((x, y))
        print(x, y)
        if x == target or y == target:
            print("Target reached!")
            return
        q.append((cap1, y)) 
        q.append((x, cap2)) 
        q.append((0, y))    
        q.append((x, 0))   
        p = min(x, cap2 - y)
        q.append((x - p, y + p))
        p = min(y, cap1 - x)
        q.append((x + p, y - p))
water_jug(4, 3, 2)




##Q2)
colors = ["Red", "Green", "Blue"]
graph = {
    1: [2, 3, 4, 5],
    2: [1, 3, 4, 5],
    3: [1, 2, 4, 5],
    4: [1, 2, 3, 5],
    5: [1, 2, 3, 4]
}
assignment = {}
def is_safe(vertex, color):
    for neighbor in graph[vertex]:
        if neighbor in assignment:
            if assignment[neighbor] == color:
                return False
    return True
def backtracking(vertices, index):
    if index == len(vertices):
        return True
    vertex = vertices[index]
    for color in colors:
        if is_safe(vertex, color):
            assignment[vertex] = color

            if backtracking(vertices, index + 1):
                return True
            del assignment[vertex]
    return False
vertices = [1, 2, 3, 4, 5]
if backtracking(vertices, 0):
    print("CSP Solution:")
    for vertex in vertices:
        print("Vertex", vertex, "=", assignment[vertex])
else:
    print("No solution exists.")
    
    
    
 ##Q2(OR)
class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
    def add_child(self, child):
        self.children.append(child)
    def display(self, level=0):
        print(" " * level + str(self.value))
        for child in self.children:
            child.display(level + 2)
root = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")
root.add_child(b)
root.add_child(c)
b.add_child(d)
b.add_child(e)
print("Game Tree:")
root.display()
  