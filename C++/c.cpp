#include<bits/stdc++.h>

using namespace std;
int main()
{
    int a[1000];
    int n;
    cin>>n;
    for (int i = 0; i < n; i++)
    {
        cin>>a[i];
    }
    int sum = 0;
    int multi = 1;
    double ave = 0;
    for (int i = 0; i < n; i++)
    {
        sum+=a[i];
        multi *= a[i];
        ave = sum/n;
    }
    cout<<sum<<" "<<multi<<" "<<ave;
    return 0;
}
//Nhập vào số lượng phần tử và giá trị từng phần tử của mảng. In ra màn hình tổng, tích và giá trị trung bình của mảng đó.
