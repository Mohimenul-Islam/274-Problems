#include <bits/stdc++.h>
using namespace std;
using ll = long long;
const int N = 2e5 + 10;

void solve() {
  int n, m; cin >> n >> m;
  int adj[n][n]{};
  for (int i = 0; i < m; ++i) {
    int u, v; cin >> u >> v;
    --u, --v;
    adj[u][v] = 1, adj[v][u] = 1;
  }
  int MASK = (1 << n), ans = 0;
  for (int mask = 0; mask < MASK; ++mask) {
    vector <int> v;
    for (int i = 0; i < n; ++i) {
      if (mask & (1 << i)) v.push_back(i);
    }
    int len = v.size();
    // cout << len << ' ' << '\n';
    bool f = true;
    for (int i = 0; i < len; ++i) {
      for (int j = i + 1; j < len; ++j) f &= adj[v[i]][v[j]];
    }
      if (f) ans = max(ans, len);
  }
  cout << ans << '\n';
}
int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int t = 1; 
  // cin >> t;
  while (t--)
  solve();
}