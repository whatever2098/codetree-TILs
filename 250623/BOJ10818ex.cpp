#include <bits/stdc++.h>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
  ios_base::sync_with_stdio(0);
  cin.tie(0); cout.tie(0);

  int N;
  cin >> N;
  vector<int> nums(N);
  for(int i = 0; i < N; ++i){
          cin >> nums[i];
  }
      
  sort(nums.begin(), nums.end());
  cout << nums[0] << " " << nums[N - 1] << "\n";

}