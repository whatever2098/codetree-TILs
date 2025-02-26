#include <iostream>
#include <string>

using namespace std;

string user2_id;
int user2_level;

class User {
    public:
    string id_;
    int level_;

    User(string id,int level){
        this->id_ = id;
        this->level_ = level;
    }
};

int main() {
    cin >> user2_id >> user2_level;

    User user1 = User("codetree", 10);
    User user2 = User(user2_id, user2_level);

    cout << "user " << user1.id_ << " lv " << user1.level_ << "\n"
    <<"user " << user2.id_ << " lv " <<user2.level_ << "\n";

    return 0;
}