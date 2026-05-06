#include <iostream>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int dx[4] = { 1, 0, -1, 0 };
    int dy[4] = { 0, -1, 0, 1 };
    int x{ 0 };
    int y{ 0 };

    int N;
    cin >> N;

    for(int i{0};i < N;i++){
        char dir;
        int dist;
        cin >> dir >> dist;

        int dir_c;
        if(dir == 'E'){dir_c = 0;}
        else if(dir == 'S'){dir_c = 1;}
        else if(dir == 'W'){dir_c = 2;}
        else{dir_c = 3;}

        x += (dx[dir_c] * dist);
        y += (dy[dir_c] * dist);
    }

    cout << x << " " << y;
    return 0;
}