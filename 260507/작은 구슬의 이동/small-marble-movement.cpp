#include <iostream>
using namespace std;

int main() {
    int N, T;
    cin >> N >> T;

    int x, y;
    char D;
    cin >> x >> y >> D;

    while(T--){
        int nx = x;
        int ny = y;

        if(D == 'U') nx--;
        else if(D == 'D') nx++;
        else if(D == 'R') ny++;
        else if(D == 'L') ny--;

        if(nx < 1 || nx > N || ny < 1 || ny > N){
            if(D == 'U') D = 'D';
            else if(D == 'D') D = 'U';
            else if(D == 'R') D = 'L';
            else if(D == 'L') D = 'R';
        }
        else{
            x = nx;
            y = ny;
        }
    }
    cout << x << " " << y << "\n";
}