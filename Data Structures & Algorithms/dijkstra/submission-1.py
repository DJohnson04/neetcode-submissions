import heapq
class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        dist = [float('inf')] * n 
        dist[src] = 0
        pq = []
        heapq.heappush(pq, (0, src))
        ((0, src))
        while pq:
            distan, vertex = heapq.heappop(pq)
            if distan > dist[vertex]:
                continue
            for edge in edges:
                if edge[0] == vertex:
                    d = edge[2]
                    v = edge[1]
                    if dist[v] > distan + d:
                        dist[v] = distan + d
                        heapq.heappush(pq, (dist[v], v))
        returned_dic = {}
        for index, distance in enumerate(dist):
            if distance == float('inf'):
                distance = -1
            returned_dic[index] = distance
        return returned_dic