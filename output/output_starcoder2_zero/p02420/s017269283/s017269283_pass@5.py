#include <iostream>
using namespace std;
 
int main()
{
    int m;
 
    string s;

    while (cin >> s) {
        if (s == "-") break;

        cin >> m;
 
        for (int i = 0; i < m; ++i) {
            char temp;

            int n;
            cin >> n;
 
            temp = s[n];
            s.erase(n, 1);
            s += temp;
        }
 
        cout << s << endl;
    }
 
    return 0;
}