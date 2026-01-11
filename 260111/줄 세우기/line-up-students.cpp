#include <iostream>
#include <tuple>
#include <algorithm>
#include <vector>
using namespace std;

vector<tuple<int, int, int>> students;

bool cmp(const tuple<int, int, int>& a, const tuple<int, int, int>& b) {
	int num1, h1, w1;
	tie(num1, h1, w1) = a;
	int num2, h2, w2;
	tie(num2, h2, w2) = b;

	if (h1 != h2) return h1 > h2;
	else if (w1 != w2) return w1 > w2;
	return num1 < num2;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	int N, num, h, w;
	cin >> N;

	for (int i{ 1 }; i <= N; i++) {
		num = i;
		cin >> h >> w;
		tuple<int, int, int> student = make_tuple(num, h, w);
		students.push_back(student);
	}

	sort(students.begin(), students.end(), cmp);

	for (int i{ 0 }; i < N; i++) {
		int num, h, w;
		tie(num, h, w) = students[i];
		cout << h << " " << w <<  " " << num << "\n";
	}
}