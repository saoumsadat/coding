#include<bits/stdc++.h>
using namespace std;

int inCheck(const vector<int>& arr, int size, int num)
{
	for (int i = 0; i < size; i++) 
	{
		if (arr[i] == num)
		{
			return 1;
		}
	}
	return 0;
}

void printArr(const vector<int>& arr)
{
	for (int i = 0; i < arr.size(); i++)
		{
			cout << arr[i] << ' ';
		}
		cout << endl;
}

int main() 
{
	int t;
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		int n, m, k;
		cin >> n >> m >> k;
		int elem_count = k / 2;

		vector<int> arr1;
		vector<int> arr2;
		for (int i = 0; i < n; i++)
		{
			int num;
			cin >> num;
			if (num >= 1 && num <= k && !inCheck(arr1, arr1.size(), num))
			{
				arr1.push_back(num);
			}
		}
		for (int i = 0; i < m; i++)
		{
			int num;
			cin >> num;
			if (num >= 1 && num <= k && !inCheck(arr2, arr2.size(), num))
			{
				arr2.push_back(num);
			}
		}

		printArr(arr1);
		printArr(arr2);
		cout << endl;

		int v = 0;
		vector<int> temp_arr1;
		vector<int> temp_arr2;
		while (temp_arr1.size() <= elem_count && temp_arr2.size() <= elem_count)
		{
			for (int i = 0; i < arr1.size(); i++)
			{
				if (inCheck(arr2, arr2.size(), arr2[i]))
				{
					if (temp_arr1.size() > temp_arr2.size())
					{
						temp_arr2.push_back(arr1[i]);
					}
					else
					{
						temp_arr1.push_back(arr1[i]);
					}
				}
				else
				{
					temp_arr1.push_back(arr1[i]);
				}
			}

			for (int i = 0; i < arr2.size(); i++)
			{
				if (!inCheck(temp_arr1, temp_arr1.size(), temp_arr1[i]) && !inCheck(temp_arr2, temp_arr2.size(), temp_arr2[i]))
				{
					temp_arr2.push_back(arr2[i]);
				}
			}

			if (temp_arr1.size() == temp_arr2.size() == elem_count)
			{
				v = 1;
				break;
			}
		}
		printArr(temp_arr1);
		printArr(temp_arr2);
		cout << v << endl;
	}


  return 0;
}