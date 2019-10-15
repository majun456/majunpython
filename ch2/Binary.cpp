#include<stdio.h>
#include<stdlib.h>
using namespace std;
void main()
{
    int n=5;
    //scanf("%d",n);
   // int* a= (int*) malloc(sizeof(n));
    //int* b= (int*) malloc(sizeof(n));
    //int* c= (int*) malloc(sizeof(6));
   // scanf("%d/n",a[n]);
   // scanf("%d/n",b[n]);
    //int* a=new int[n];
    //int* b=new int[n];
    //int* c=new int[n+1];
int a[5]={1,1,0,1,1};
int b[5]={1,1,1,1,1};
int c[6]={0,0,0,0,0,0};
int tmp1=0;
int tmp2=0;
    for (int i=n-1;i>=0;i--)
    {
        
    if(i==n-1){
        tmp1=(a[i]+b[i])%2; //余数
        tmp2=(a[i]+b[i]-tmp1)/2;//进位
        c[i+1]=tmp1;
    }
    else{
    tmp1=(a[i]+b[i]+tmp2)%2 ;//余数
    tmp2=(a[i]+b[i]-tmp1)/2;//进位
    c[i+1]=tmp1;

    }
    c[0]=tmp2;

    }
  

                  }