#include<stdio.h>
long int bAdd(long int bin1,long int bin2){
    int i=0,sum[20]={0},carry=0;
    while((bin1!=0) || (bin2!=0)){
        sum[i]=(bin1%10+bin2%10+carry)%2;
        carry=(bin1%10+bin2%10+carry)/2;
        bin1/=10;
        bin2/=10;
        i++;
    }
    if(carry!=0){
        sum[i]=carry;
        i++;
    }
    i--;
    long int result=0;
    while(i>=0){
        result=result*10+sum[i--];
    }
}
long int bMul(long int bin1,long int bin2){
    long int digit,factor=1,p=0,pp;
    while(bin2!=0){
        digit=bin2%10;
        if(digit==1){
            pp=bin1*factor;
            p=bAdd(p,pp);
        }
        bin2/=10;
        factor*=10;
    }
    return p;
}
int main(){
    long int bin1,bin2;
    scanf("%ld %ld",&bin1,&bin2);
    printf("%ld",bMul(bin1,bin2));
    return 0;}