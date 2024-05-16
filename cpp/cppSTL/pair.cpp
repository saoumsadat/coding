#include <bits/stdc++.h>
using namespace std;

int main()
{
	//pair
	pair<int, int> p = {1, 3};
	cout << p.first << " " << p.second << endl;

	pair<int, pair<int,int>> pMulti = {1, {3, 5}};	//to store more than 2 values
	cout << pMulti.first << " " << pMulti.second.first << " " << pMulti.second.second << endl;

	pair<int, int> arr[] = {{1, 2}, {3, 4}, {5, 6}};	//array of pairs
	size_t size = sizeof(arr) / sizeof(arr[0]);
	for (int i = 0; i < size; i++)
	{
		cout << arr[i].first << " " << arr[i].second << endl;
	}

}