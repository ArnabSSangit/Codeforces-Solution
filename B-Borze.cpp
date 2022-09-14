#include <bits/stdc++.h>
using namespace std;
 
int main(){
    string s,t;
    cin>> s;
    int l = s.length();
    for(int i=0; i<l; i++){
        if(s[i]=='.'){
            t+='0';
        }
        if (s[i]=='-' &&s[i+1]=='.'){
            t+='1';
            i++;
        }
        if(s[i]=='-' && s[i+1]=='-'){
            t+='2';
            i++;
        }
    }
    cout<<t<<endl;
    return 0;
 
 
}
