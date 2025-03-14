#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const int N = 2e5 + 10;

int to_min(int n) {
  int tot = 0;
  tot += n % 100;
  tot += (n / 100) * 60;
  return tot;
} 

int roundUp(int n) {
  return (n + 4) / 5 * 5;
}

int roundDown(int n) {
  return n / 5 * 5;
}

string minToHour(int n) {
  int min = n % 60, hour = n / 60;
  string s = to_string(hour), t = to_string(min);
  if (s.size() == 1) s = "0" + s;
  if (t.size() == 1) t = "0" + t;
  return s + t;
}

void solve() {
  int n; cin >> n;
  vector <array<int, 2>> v(n);
  char c;
  for (int i = 0; i < n; ++i) {
    int start, end;
    cin >> start >> c >> end;
    v[i][0] = roundDown(to_min(start)), v[i][1] = roundUp(to_min(end));
  }
  sort(v.begin(), v.end());
  for (int i = 0; i < n; ++i) {
    if (i + 1 < n and v[i][1] >= v[i + 1][0]) {
      v[i + 1][0] = v[i][0];
      v[i + 1][1] = max(v[i + 1][1], v[i][1]);
    } else cout << minToHour(v[i][0]) << "-" << minToHour(v[i][1]) << '\n';
  } 
}
int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  solve();
}