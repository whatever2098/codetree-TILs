#include <iostream>
using namespace std;

void lcm(int n, int m){
    int divided = n;
    int dividing = m;
    int gcd;
    while(dividing != 0){
        int temp = dividing;
        dividing = divided % dividing;
        divided = temp;
    }
    gcd = divided;
    cout << n * m / gcd << "\n";
}

int main() {
    // 여기에 코드를 작성해주세요.
    int n, m;
    cin >> n >> m;
    lcm(n, m);
    return 0;
}