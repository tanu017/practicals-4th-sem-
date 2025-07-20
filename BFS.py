MAX = 100
c = [[0]*MAX for i in range(MAX)]
visited = [0]*MAX
queue = [0]*MAX
def BFS(v):
  front = 0
  rear = -1
  visited[v] = 1
  queue[rear+1] = v
  rear += 1
  while front <= rear: 
    v = queue[front]
    front+=1
    print(f"{v}", end=" ")
    for i in range(1, n+1):
      if c[v][i] == 1 and visited[i] == 0:
        queue[rear+1] = i
        rear+=1
        visited[v] = 1

if __name__ == "__main__":
  n = int(input("Enter the number of vertices: "))
  print("Enter the cost matrix: ")
  for i in range(1, n+1):
    c[i] = [0] + list(map(int, input().split()))
  for i in range(1, n+1):
    visited[i] = 0
  v = int(input("Enter the starting vertex: "))
  print("BFS Traversal is: ")
  BFS(v)
