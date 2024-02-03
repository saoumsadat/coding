#include<bits/stdc++.h>
using namespace std;

int main()
{
  for (int i = 0, n; cin >> n; i++)
  {
    if (n)
    {
        cout << abs(2-i/5) + abs(2-i%5);
    }
  }
}
