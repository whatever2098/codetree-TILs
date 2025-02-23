#include <iostream>
using namespace std;

int n;
int arr[10];

int GCD(int a, int b){
    if(b == 0) return a; 
    return GCD(b, a % b);
}

int main() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    int lcm{ arr[0] };
    for ( int i = 0; i < n - 1; i++) {
        lcm = lcm * arr[i + 1] / GCD(lcm, arr[i + 1]);
    }
    cout << lcm << "\n";
    
    return 0;
}