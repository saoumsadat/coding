#include <bits/stdc++.h>
using namespace std;

void nForest(int n)
{
	// Write your code here.
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			cout << "* ";
		}
		cout << '\n';
	}
}

void nStarTriangle(int n)
{
	// Write your code here.
	int h = 2 * n - 1;
	for (int i = n; i > 0; i--)
	{
		for (int j = h; j > 0; j--)
		{
			if (j > (n - i) && j < (n + i))
			{
				cout << '*';
			}
			else
			{
				cout << ' ';
			}
		}
		cout << endl;
	}
}
void pattern10(int n)
{
	for (int i = 0; i < (2 * n - 1); i++)
	{
		int end;
		if (i < n)
			end = i + 1;
		else
			end = (n - (i - n)) - 1;

		for (int j = 0; j < end; j++)
		{
			cout << '*';
		}

		cout << endl;
	}
}

void pattern11(int n)
{
	for (int i = 0; i < n; i++)
	{
		int out = !(i % 2);
		for (int j = 0; j <= i; j++)
		{
			cout << out << ' ';
			out = !out;
		}
		cout << endl;
	}
}

void pattern12(int n)
{
	for (int i = 1; i <= n; i++)
	{
		int j = 1;
		while (j <= i)
		{
			cout << j;
			j++;
		}
		while (j <= (2 * n - i))
		{
			cout << ' ';
			j++;
		}
		while (j <= (2 * n))
		{
			cout << ((2 * n) - j + 1);
			j++;
		}
		cout << endl;
	}
}

void pattern13(int n)
{
	int out = 1;
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j <= i; j++)
		{
			cout << out << ' ';
			out++;
		}
		cout << endl;
	}
}

void pattern14(int n)
{
	cout << char(n);
}

int main()
{
	int x;
	cin >> x;
	pattern14(x);
}