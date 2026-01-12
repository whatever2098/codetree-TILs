#include <iostream>
#include <algorithm>
#include <tuple>
#include <cmath>
#include <vector>
using namespace std;

vector<tuple<int, int, int>> v;

bool cmp(tuple<int, int, int> a, tuple<int, int, int> b) {
	int idx1, idx2, x1, x2, y1, y2;
	tie(idx1, x1, y1) = a;
	tie(idx2, x2, y2) = b;

	int distance1 = abs(x1) + abs(y1);
	int distance2 = abs(x2) + abs(y2);

	if (distance1 != distance2) {
		return distance1 < distance2;
	}
	
	return idx1 < idx2;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

    v.clear();
	int N;
	cin >> N;
	for (int i{ 1 }; i <= N; i++) {
		int x, y;
		cin >> x >> y;
		v.push_back({ i, x, y });
	}

	sort(v.begin(), v.end(), cmp);

	for (auto e : v) {
		cout << get<0>(e) << "\n";
	}
}