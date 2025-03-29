#include <iostream>
using namespace std;
string x;
int main() {
    cin >> x;
    string ans = "";
    for (auto v : x) {
        if (isupper(v))
            ans += tolower(v);
        else if (islower(v))
            ans += toupper(v);
        else
            ans += v;
    }
    cout << ans << endl;
}