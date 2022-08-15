import heapq
def dijkstra(graph, distance):
    q = []
    heapq.heappush(q, (0, 1))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        distance[now] = dist
        
        for b, c in graph[now]:
            cost = dist + c
            if cost < distance[b]:
                distance[b] = cost
                heapq.heappush(q, (cost, b))
                
def solution(N, road, K):
    answer = 0
    distance = [float('inf')] * (N + 1)
    graph = [[] for _ in range(N + 1)]
    print(distance)
    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))
    print(graph)
    
    dijkstra(graph, distance)
    return len([dist for dist in distance if dist <= K])
'''
example
'''
N = 5
road = 	[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
K = 3
print(solution(N,road,K))
