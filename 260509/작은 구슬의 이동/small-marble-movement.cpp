#include <iostream>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	int N, T;
	cin >> N >> T;

	int R, C;
	char inputD;
	cin >> R >> C >> inputD;

	int dx[4] = { -1, 1, 0, 0 }; //0123
	int dy[4] = { 0, 0, 1, -1 }; //UDRL

	int D{ 0 };
	if (inputD == 'U') D = 0;
	else if (inputD == 'D') D = 1;
	else if (inputD == 'R') D = 2;
	else if (inputD == 'L') D = 3;

	int x = R - 1;
	int y = C - 1;

	while (T--) {
		int new_x = x + dx[D];
		int new_y = y + dy[D];

		if (new_x < 0 || new_x >= N || new_y < 0 || new_y >= N) {
			if (D == 0 || D == 2) { D += 1; }
			else if (D == 1 || D == 3) { D -= 1; }
			continue;
		}

		x = new_x;
		y = new_y;
	}
	cout << x + 1 << " " << y + 1 << "\n";
}