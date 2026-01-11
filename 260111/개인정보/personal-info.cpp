#include <iostream>
#include <tuple>
#include <algorithm>
#include <vector>
using namespace std;

vector<tuple<string, int, double>> students;

bool cmp1(const tuple<string, int, double>& a, const tuple<string, int, double>& b) {
	string name1, name2;
	int h1, h2;
	double w1, w2;
	tie(name1, h1, w1) = a;
	tie(name2, h2, w2) = b;

	return name1 < name2;
}

bool cmp2(const tuple<string, int, double>& a, const tuple<string, int, double>& b) {
	string name1, name2;
	int h1, h2;
	double w1, w2;
	tie(name1, h1, w1) = a;
	tie(name2, h2, w2) = b;

	return h1 > h2;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	string name;
	int h;
	double w;
	for (int i{ 0 }; i < 5; i++) {
		cin >> name >> h >> w;
		tuple<string, int, double> student = make_tuple(name, h, w);
		students.push_back(student);
	}

	sort(students.begin(), students.end(), cmp1);

	cout << "name" << "\n";
	for (int i{ 0 }; i < 5; i++) {
		tie(name, h, w) = students[i];
		cout << name << " " << h <<  " " << w << "\n";
	}

	sort(students.begin(), students.end(), cmp2);

	cout << "\n" << "height" << "\n";
	for (int i{ 0 }; i < 5; i++) {
		tie(name, h, w) = students[i];
		cout << name << " " << h << " " << w << "\n";
	}
}