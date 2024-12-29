def minCostConnectPoints(points):
    distances_dict = {}
    for index, point in enumerate(points):
        val = abs(0 - point[0]) + abs(0 - point[1])
        distances_dict[index] = val

    sorted_dict = dict(sorted(distances_dict.items(), key=lambda item: item[1]))
    final_result = 0
    for key in sorted_dict.keys():
        final_result += abs(0 - points[key][0]) + abs(0 - points[key][1]) 
        print(final_result)
    return final_result


points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
result = minCostConnectPoints(points=points)
print(result)

