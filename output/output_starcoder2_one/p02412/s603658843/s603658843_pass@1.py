#include <iostream>
using namespace std;
int main(){
    int n,x;
    while(cin>>n>>x){
        if(n==0 && x==0) break;
        cout<<(n+1)*(n+2)/2-(n-x)*(n-x+1)/2<<endl;
    }
}