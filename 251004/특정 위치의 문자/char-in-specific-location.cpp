#include <iostream>
using namespace std;

static char arr[6] = {'L', 'E', 'B', 'R', 'O', 'S'};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);

    char p;
    cin >> p;

    int idx = -1;

    for (int i{0};i < 6;i++){
        if(arr[i] == p){
            idx = i;
            cout << idx <<"\n";
            break;
        }
    }
    if(idx == -1){
        cout << "None" << "\n";
    }
    return 0;
}