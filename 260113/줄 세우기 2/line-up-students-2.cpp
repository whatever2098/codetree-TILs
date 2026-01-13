#include <iostream>
#include <vector>
#include <tuple>
#include <algorithm>
using namespace std;

vector<tuple<int, int, int>> v;

bool cmp(const tuple<int, int, int>& a, const tuple<int, int, int>& b) {
	if (get<1>(a) != get<1>(b)) return get<1>(a) < get<1>(b);
	if (get<2>(a) != get<2>(b)) return get<2>(a) > get<2>(b);
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	int N;
	cin >> N;
	for (int i{ 1 }; i <= N; i++) {
		int num, h, w;
		num = i;
		cin >> h >> w;
		v.push_back({ num, h, w });
	}

	sort(v.begin(), v.end(), cmp);

	for(auto e : v) {
		cout << get<1>(e) << " " << get<2>(e) << " " << get<0>(e)
			<< "\n";
	}
}
