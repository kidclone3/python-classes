def triangulate_polygon(polygon):
    if len(polygon) < 3:
        return 0
    min_cost = float('inf')
    for i in range(1, len(polygon) - 1):
        cost = triangulate_polygon(polygon[:i+1]) + triangulate_polygon(polygon[i:]) + polygon[0] * polygon[i] * polygon[-1]
        min_cost = min(min_cost, cost)
    return min_cost