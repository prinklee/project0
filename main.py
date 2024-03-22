#distance to each vertex
matrix = [[0, 2, 3, 0, 0, 20], [2, 0, 7, 0, 4, 0], [3, 7, 0, 1, 0, 0], [0, 0, 1, 0, 0, 5], [0, 4, 0, 0, 0, 6], [20, 0, 0, 5, 6, 0]]

print(*matrix, sep="\n")
print("\n")

dist = [0, -1, -1, -1, -1, -1]

vertices = {0}

while vertices != {0,1,2,3,4,5}:

  for x in vertices.copy():
    count = 0
    for i in matrix[x]:
      if i > 0:
        vertices.add(count)
        if dist[count] == -1:
          dist[count] = i + dist[x]
        elif dist[x] + i < dist[count]:
          dist[count] = dist[x] + i
      count = count+1
  print(dist)

for x in vertices.copy():
  count = 0
  for i in matrix[x]:
    if i > 0:
      vertices.add(count)
      if dist[count] == -1:
        dist[count] = i + dist[x]
      elif dist[x] + i < dist[count]:
        dist[count] = dist[x] + i
    count = count+1

print(dist)
