#include <bits/stdc++.h>
using namespace std;
int N = 20;

const int dx[8] = {1,1,2,2,-1,-1,-2,-2};
const int dy[8] = {2,-2,1,-1,2,-2,1,-1};

bool inside(int x, int y)
{
	return ((x >= 0 && y >= 0) && (x < N && y < N));
}

bool isValid(int a[], int x, int y)
{
	return (inside(x, y)) && (a[y*N+x] < 0);
}

int getDegree(int a[], int x, int y)
{
	int count = 0;
	for (int i = 0; i < N; ++i)
		if (isValid(a, (x + dx[i]), (y + dy[i])))
			count++;

	return count;
}

bool nextMove(int a[], int *x, int *y)
{
	int min_deg_idx = -1, c, min_deg = (N+1), next_x, next_y;

	int start = rand()%N;
	for (int count = 0; count < N; ++count)
	{
		int i = (start + count)%N;
		next_x = *x + dx[i];
		next_y = *y + dy[i];
		if ((isValid(a, next_x, next_y)) && (c = getDegree(a, next_x, next_y)) < min_deg)
		{
			min_deg_idx = i;
			min_deg = c;
		}
	}

	if (min_deg_idx == -1)
		return false;

	next_x = *x + dx[min_deg_idx];
	next_y = *y + dy[min_deg_idx];

	a[next_y*N + next_x] = a[(*y)*N + (*x)]+1;

	*x = next_x;
	*y = next_y;

	return true;
}

void print(int a[])
{
	for (int i = 0; i < N; ++i)
	{
		for (int j = 0; j < N; ++j)
            cout << a[j*N+i] << " \n"[j == N-1];
	}
}

bool neighbour(int x, int y, int xx, int yy)
{
	for (int i = 0; i < N; ++i)
		if (((x+dx[i]) == xx)&&((y + dy[i]) == yy))
			return true;

	return false;
}
int loopCount = 0;
bool found = 0;
bool findClosedTour()
{
	int a[N*N];
	for (int i = 0; i< N*N; ++i)
		a[i] = -1;

	int sx = 0;
	int sy = 0;

	int x = sx, y = sy;
	a[y*N+x] = 0; // Mark first move.

	for (int i = 0; i < N*N-1; ++i)
		if (nextMove(a, &x, &y) == 0)
			return false;

	if (!neighbour(x, y, sx, sy))
		return false;

    found = true;
	print(a);
	return true;
}

int main()
{
	srand(time(NULL));

	// While we don't get a solution
	while (!findClosedTour() || loopCount++ > 1000)
	{
	loopCount++;
	}
    if (!found) cout << "Not found!";
	return 0;
}
