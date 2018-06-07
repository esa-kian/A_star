print """A* search:
               Oradea to Craiova"""
#فراخواني نقشه و هيورستيک از ماژول تعريف شده
from ROMANIA import MAP, SLD
#فراخواني ماژول براي کار با صف
import heapq
#تعريف کلاس براي کار نقشه
class PriorityQueue:

    #تعريف صف اوليه خالي 
    def __init__(self):
        self.elements = []
        
    #خالي کردن صف
    def empty(self):
        return len(self.elements) == 0

    #افزودن به صف 
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    #پاپ کرده سپس برميگرداند
    def get(self):
        return heapq.heappop(self.elements)[1]

#تعريف تابع هيورستيک
def h(edge):
	return SLD[edge]

#نشان دادن مسير حرکت
def traverse(parent, start, goal):
    path = [goal]
    while path[-1] != start:
        path.append (parent[path[-1]])
    path.reverse()
    return path


def astar(G, start, goal):
	frontier = PriorityQueue()
	parent 	 =  {}
	visited  = set()
	#جمع کردن هزينه
	frontier.put (start, 0)
	#شهرهاي ملاقات شده
	visited.add(start)
	while not frontier.empty():
		vertex = frontier.get()
		if vertex == goal:
			return traverse(parent, start, goal)
		for edge in G[vertex]:
			if edge not in visited:				
				cost = h(edge) + G[vertex][edge]
				frontier.put(edge, cost)
				parent[edge] = vertex
				visited.add(edge)
	return None

if __name__ == '__main__':
	print astar(MAP, "Oradea", 'Craiova')
	


