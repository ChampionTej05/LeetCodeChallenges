'''
https://leetcode.com/problems/cheapest-flights-within-k-stops/?envType=daily-question&envId=2024-02-22


We need the flight to be cheapest from current vertex based on two params 
    - distance (cost)
    - stops remaining 
    
Can we use PQ here  ? 

If at every node, we store (cost, hops)
where cost = minimum cost needed to reach this node from src 
hops = minimum hops needed to reach this node from src 

We can return the answer node[dest][cost] if node[dest][hopes] <=k 

At each node, before updating, we can check this condition 

if node[dest][cost] <= incoming_cost and incoming_hops+1 <= k :
        then update hops and cost 
        
set distance to infinity for all the nodes  

'''

from collections import defaultdict, deque
class Graph:
    
    def __init__(self, V) :
        self.V = V 
        self.graph = defaultdict(list)
        self.node_distances = [float("inf")]*self.V
        
    def add_edge(self, src, dest, weight):
        self.graph[src].append((dest, weight))
        
        
    def traverse(self, src, dest, hops):
        maximum_allowed_hops = hops+1
        
        queue = deque()
        queue.append((src, 0))
        self.node_distances[src] = 0 
        # distance = [float("inf")]*self.V 
        while maximum_allowed_hops>0 and  queue:
            print("Queue {} , when hops remaining = {}".format(queue, maximum_allowed_hops))
            level_nodes = len(queue)
            
            for i in range(level_nodes):
                node, node_price = queue.popleft()
                for neigbour, price in self.graph[node]:
                    new_node_price = node_price + price 
                    if new_node_price < self.node_distances[neigbour]:
                        self.node_distances[neigbour] = new_node_price
                        queue.append((neigbour, new_node_price))
                        
            maximum_allowed_hops-=1
            
        return self.node_distances[dest] if self.node_distances[dest] != float("inf") else -1 

class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """

        graph = Graph(n)
        for flight in flights:
            graph.add_edge(flight[0], flight[1], flight[2])

        print("Graph", graph)
        

        cheapest_price = graph.traverse(src, dst, k)
        return cheapest_price
                    
               
        
    
        
n = 4 
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src = 0 
dst =3 
k = 1

obj = Solution()
print(obj.findCheapestPrice(n, flights, src, dst, k))