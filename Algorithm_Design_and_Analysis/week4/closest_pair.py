import sys
import math
 
# To find the closest pair of points
def closestPair(coordinates, n):
   
    # List of pairs to store points on plane
    points = [(coordinates[i][0], coordinates[i][1]) for i in range(n)]
 
    # Sort them according to their x-coordinates
    points.sort()
 
    # Minimum distance b/w points seen so far
    d = sys.maxsize
 
    # Keeping the points in increasing order
    st = set()
    st.add(points[0])
 
    for i in range(1, n):
        l = set([p for p in st if p[0] >= points[i][0]-d and p[1] >= points[i][1]-d])
        r = set([p for p in st if p[0] <= points[i][0]+d and p[1] <= points[i][1]+d])
        intersection = l & r
        if len(intersection) == 0:
            continue
 
        for val in intersection:
            dis = math.pow(points[i][0] - val[0], 2) + math.pow(points[i][1] - val[1], 2)
 
            # Updating the minimum distance dis
            if d > dis:
                d = dis
 
        st.add(points[i])
 
    return d
 
# Points on a plane P[i] = (x, y)
P = [(1, 2), (2, 3), (3, 4), (5, 6), (2, 1)]
n = len(P)
 
# Function call
print("The smallest distance is", closestPair(P, n))