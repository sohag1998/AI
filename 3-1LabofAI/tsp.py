import itertools
import sys

n = int(input())
dist = [list(map(int, input().split())) for _ in range(n)]
tour = list(range(n))

bestDist = sys.maxsize  # best tour distance
bestTour = list(range(n))  # best tour

for perm in itertools.permutations(tour[1:]):
    tour[1:] = perm
    tourDist = 0  # current tour distance

    for i in range(n - 1):
        tourDist += dist[tour[i]][tour[i + 1]]

    tourDist += dist[tour[n - 1]][tour[0]]  # return to starting city

    if tourDist < bestDist:
        bestDist = tourDist
        bestTour = tour[:]

print("Best tour distance:", bestDist)
print("Best tour:", end=" ")

for i in bestTour:
    print(i, end=" ")

print()
