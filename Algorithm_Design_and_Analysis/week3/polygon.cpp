#include <iostream>
#include <cmath>
#include <vector>
#define MAX 1000000.0
using namespace std;

const double INF = 1e18;

// Structure of a point in 2D plane
struct Point
{
	int x, y;
};

vector<vector<bool>> check;

bool check_points(int i, int j) {
    return i + 1 == j || check[i][j] || check[j][i];
}

// A utility function to find distance between two points in a plane
double dist(Point p1, Point p2)
{
	return sqrt((p1.x - p2.x)*(p1.x - p2.x) +
				(p1.y - p2.y)*(p1.y - p2.y));
}

// Recursive function, with check_points function to avoid duplicate diagonal.
double triangulate_polygon(Point points[], int n, int i, int j) {
    if (j <= i + 2) {
        return 0;
    }
    
    double min_cost = INF;
    for (int k = i + 2; k < j; k++) {
        double cur_cost = 0.0;
        bool mod1, mod2;
        mod1 = mod2 = false;
        if (!check_points(i, k)) {
            mod1 = true;
            check[i][k] = 1;
            cur_cost += dist(points[i], points[k]);
        }
        if (!check_points(k, j)) {
            mod2 = true;
            check[k][j] = 1;
            cur_cost += dist(points[k], points[j]);
        }
        double left = triangulate_polygon(points, n, i, k);
        double right = triangulate_polygon(points, n, k, j);
        double cost = left + right + cur_cost;
        // Return the before state.
        if (mod1) check[i][k] = 0; 
        if (mod2) check[k][j] = 0; 

        min_cost = min(min_cost, cost);
    }
    return min_cost;
}


// Driver program to test above functions
int main()
{
    // freopen("input.txt", "r", stdin);
    int n; cin >> n;
    check.resize(n, vector<bool>(n, 0));

	Point points[n];
    for(int i = 0; i < n; ++i) {
        int x, y; cin >> x >> y;
        points[i] = {x, y};
    }
	// cout << mTC(points, 0, n-1);
    double ans = triangulate_polygon(points, n, 0, n-1);
    cout << ans;
	return 0;
}