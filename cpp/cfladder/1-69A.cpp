#include<bits/stdc++.h>
using namespace std;

int main()
{
  int n;
  cin >> n;
  int x = 0, y = 0, z = 0;
  int arr[n * 3];

  for (int i = 0; i < (n * 3); i++)
  {
    cin >> arr[i];
  }
  
  int i = 0;
  while (i < (n * 3))
  {
    x += arr[i];
    i++;
    y += arr[i];
    i++;
    z += arr[i];
    i++;
  }

  if (!x && !y && !z)
  {
    cout << "YES";
  }
  else
  {
    cout << "NO";
  }
}