#include<bits/stdc++.h>
using namespace std;

void doSomething(int &x) {
  cout << x << endl;
  x++;
  cout << x << endl;
  x++;
  cout << x << endl;
}

int main() {
  int x = 10;
  doSomething(x);
  cout << x << endl;
}