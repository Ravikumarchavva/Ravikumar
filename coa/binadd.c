#include<stdio.h>
int main(){
    int bin1,bin2,i=0,sum[20],carry=0;
    scanf("%d %d",&bin1,&bin2);
    while((bin1!=0) || (bin2!=0)){
        sum[i]=(bin1%10+bin2%10+carry)%2;
        carry=(bin1%10+bin2%10+carry)/2;
        bin1=bin1/10;
        bin2=bin2/10;
        i++;
    }
    if(carry!=0){
        sum[i]=carry;
        i++;
    }
    i--;
    printf("%d\n",i);
    while(i>=0){
        printf("%d \t\t",sum[i--]);
    }
    return 0;
}