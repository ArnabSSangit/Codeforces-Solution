#include <bits/stdc++.h>
using namespace std;
int main(){
    const string probability[7] ={"", "1/1", "5/6", "2/3", "1/2", "1/3", "1/6"};
    int a,b;
    cin >> a >> b;
    int d =max(a,b);
    cout<<probability[d]<<endl;
    return 0;
}
