def travelling_salesman_approx(distance_matrix):
    n = len(distance_matrix)
    visited = [False] * n
    tour = [0]
    visited[0] = True

    for _ in range(1, n):
        last_city = tour[-1]
        next_city = -1
        min_dist = float('inf')

        for i in range(n):
            if not visited[i] and distance_matrix[last_city][i] < min_dist:
                min_dist = distance_matrix[last_city][i]
                next_city = i
        tour.append(next_city)
        visited[next_city] = True
    tour.append(tour[0])
    return tour
#Example usage
distance_matrix = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
tour = travelling_salesman_approx(distance_matrix)
print("Optimal tour:", tour)