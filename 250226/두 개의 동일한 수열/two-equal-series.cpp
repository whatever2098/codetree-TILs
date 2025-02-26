#include <iostream>
#include <algorithm>
using namespace std;

int n;
int A[100];
int B[100];

int main() {
    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> A[i];
    }

    for (int i = 0; i < n; i++) {
        cin >> B[i];
    }

    sort(A, A + n);
    sort(B, B + n);

    bool same{ true };
    for (int i = 0; i < n; i++){
        if(A[i] != B[i]){ same = false; break; } 
    }
    cout << ((same)? "Yes" : "No") << "\n";

    return 0;
}