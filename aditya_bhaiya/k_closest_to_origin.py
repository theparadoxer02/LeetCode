def kClosest(points, k):
    distances = []
    for index, point in enumerate(points):
        val = point[0] * point[0] + point[1] * point[1]
        distances.append((val, index))


    sorted_list_of_tuples = sorted(distances, key=lambda x: x[0])

    final_result = []
    for index_point in sorted_list_of_tuples[:k]:
        final_result.append(points[index_point[1]])

    return final_result

points = [[1,3],[-2,2]]
k = 1
result = kClosest(points=points, k=k)
print(result)