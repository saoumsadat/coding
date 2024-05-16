#include <bits/stdc++.h>
using namespace std;

void printVec(vector<int> v)
{
	if (!(v.size()))
	{
		cout << "No element" << endl;
		return;
	}
	for (int i = 0; i < v.size(); i++)
	{
		cout << v[i] << " ";
	}
	cout << endl;
}

int main()
{
	//vector
	vector<int> v = {10, 20, 13, 5, 4, 3};
	v.push_back(1);
	v.emplace_back(2);
	//both kinda same BUT

	vector<pair<int, int>> vp;
	vp.push_back({1, 2});
	vp.emplace_back(1, 2);
	//syntactical difference

	vector<int> ve(5); //{0, 0, 0, 0, 0}
	vector<int> v20(5, 20);	//{20, 20, 20, 20, 20}
	vector<int> vc(v20);	//store a copy of v20 in vc so: {20, 20, 20, 20, 20}
	
	//accessing values v[i] - check function
	printVec(v);

	//through iterator
	//{10, 20, 13, 5, 4, 3, 1, 2}
	vector<int>::iterator it = v.begin();	//memory address of the first element
	cout << *(it) << endl;	//10
	it = it + 2;
	cout << *(it) << endl;	//13

	it = v.end();	//memory address of the NEXT OF THE LAST element
	cout << *(it - 1) << endl;	//2

	//looping using iterator
	for (auto it = v20.begin(); it != v20.end(); it++)	//auto assigns datatype automatically - here as a pointer
	{
		cout << *(it) << " ";
	}
	cout << endl;

	//using for each loop
	for (auto it : vc)	//here auto assigns it as int
	{
		cout << it << " ";
	}
	cout << endl;

	//deletion
	v.erase(v.begin() + 1);	//takes a memory address - here removes the index 1 element
	printVec(v);
	v.emplace_back(25);
	
	v.erase(v.begin() + 2, v.begin() + 6);	//removes from i=2 to i=5 [start, end)
	printVec(v);

	//insertion
	v.insert(v.begin() + 1, 11);	//(index, element)
	v.insert(v.begin() + 2, 4, 14);	//(index, occurences, element)
	v.insert(v.begin(), vc.begin(), vc.begin() + 2);	//inserting another vector -> (index, start, end)
	printVec(v);

	//other
	v.pop_back();	//pops out last element
	v.swap(vc);	//swaps with other vector
	v.clear();	//clears the whole vector
	cout << v.empty() << endl;	//returns if the vector is empty
	printVec(vc);
	printVec(v);
}