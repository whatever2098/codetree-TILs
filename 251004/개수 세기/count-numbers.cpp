#include <iostream>
using namespace std;

static int arr[101];

int main() {
    int N, M;
    cin >> N >> M;

    int numCnt{0};
    for(int i{0};i < N;i++){
        int e;
        cin >> e;
        if(e == M) {
            numCnt++;
        }
    }

    cout << numCnt << "\n";
    return 0;
}