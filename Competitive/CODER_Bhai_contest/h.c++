#include<iostream>
#include<cstdio>
#include<algorithm>
using namespace std;
const int MAX_KNIGHTS=100005;
int num;
long long maxRounds;
int strength[MAX_KNIGHTS];
long long duelCount[MAX_KNIGHTS];

bool isPossible(long long minDuelCount) {
    long long totalDuels=0;
    for(int i=1; i<=num; i++)
        duelCount[i]=0;
    for(int i=1; i<=num; i++)
        if(duelCount[i]<minDuelCount) {
            long long requiredDuels=(minDuelCount-duelCount[i]+strength[i]-1)/strength[i];
            totalDuels+=requiredDuels*2-1;
            if(totalDuels>maxRounds) return false;
            duelCount[i+1]+=strength[i+1]*(requiredDuels-1);
        }
        else totalDuels++;
    return true;
}

void arrangeDuels() {
    cin>>num>>maxRounds;
    for(int i=1; i<=num; i++)
        cin>>strength[i];
    long long left=1, right=*max_element(strength+1, strength+num+1)*maxRounds, answer=0;
    while(left<=right) {
        long long mid=(left+right)/2;
        if(isPossible(mid)) answer=mid, left=mid+1;
        else right=mid-1; 
    }
    cout<<answer<<"\n";
    return;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr), cout.tie(nullptr);
    int testCases;
    cin>>testCases;
    while(testCases--)
        arrangeDuels();
    return 0;
}
