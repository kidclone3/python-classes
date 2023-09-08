class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
 
# A utility function to find next to top in a stack
def nextToTop(S):
    a = S.pop()
    b = S.pop()
    S.append(a)
    return b
 
# A utility function to swap two points
def swap(p1, p2):
    return p2, p1
 
# A utility function to return square of distance between
# two points
def distSq(p1, p2):
    return (p1.x - p2.x) * (p1.x - p2.x) + (p1.y - p2.y) * (p1.y - p2.y)
 
# Prints convex hull of a set of n points.
def convexHull(points, n):
 
    # There must be at least 3 points
    if (n < 3):
        return
 
    # Initialize Result
    hull = []
 
    # Find the leftmost point
    l = 0
    for i in range(1, n):
        if (points[i].x < points[l].x):
            l = i
 
    # Start from leftmost point, keep
    # moving counterclockwise until
    # reach the start point again
    # This loop runs O(h) times where h is
    # number of points in result or output.
    p = l
    q = 0
    while (True):
 
        # Add current point to result
        hull.append(points[p])
 
        # Search for a point 'q' such that
        # orientation(p, x, q) is counterclockwise
        # for all points 'x'. The idea is to keep
        # track of last visited most counterclock-
        # wise point in q. If any point 'i' is more
        # counterclock-wise than q, then update q.
        q = (p + 1) % n
 
        for i in range(0, n):
 
            # If i is more counterclockwise than
            # current q, then update q
            if (orientation(points[p], points[i], points[q]) == 2):
                q = i
 
        # Now q is the most counterclockwise with
        # respect to p. Set p as q for next iteration,
        # so that q is added to result 'hull'
        p = q
 
        # While we don't come to first point
        if (p == l):
            break
 
    # Print Result
    printHull(hull)
 
# To find orientation of ordered triplet (p, q, r).
# The function returns following values
# 0 --> p, q and r are colinear
# 1 --> Clockwise
# 2 --> Counterclockwise
 
 
def orientation(p, q, r):
    val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
 
    if (val == 0):
        return 0  # colinear
    elif (val > 0):
        return 1   # clock or wise
    else:
        return 2   # counterclock or wise
 
# Prints convex hull of a set of n points.
def printHull(hull):
 
    print("The points in Convex Hull are:")
    for i in range(len(hull)):
        print("(", hull[i].x, ", ", hull[i].y, ")")
 
# Driver Code
if __name__ == "__main__":
 
    points = [Point(0, 3), Point(2, 2), Point(1, 1), Point(2, 1), Point(3, 0), Point(0, 0), Point(3, 3)]
 
    n = len(points)
    convexHull(points, n)