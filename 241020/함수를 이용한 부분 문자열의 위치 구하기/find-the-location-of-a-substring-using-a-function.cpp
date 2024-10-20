#include <iostream>
using namespace std;

string input;
string part;

int partIndex(){
    for(int i{0};i < input.length();i++){
        if(input[i] != part[0]) continue;

        if(i + part.length() > input.length()){ return -1; }
        int index{ i };
        for(int j{1};j < part.length();j++){
            if(input[i + j] != part[j]) index = -1; break;
        }
        if(index != -1){ return index; }
    }
    return -1;
}
int main() {
    // 여기에 코드를 작성해주세요.
    cin >> input >> part;
    cout << partIndex() << "\n";
    return 0;
}