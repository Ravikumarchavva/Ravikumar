#include<stdio.h>
int main(){
    int bitA,bitB,sum,carry;
    printf("A B sum carry\n");
    for(bitA=0;bitA<=1;bitA++){
        for(bitB=0;bitB<=1;bitB++){
            sum=bitA^bitB;
            carry=bitA & bitB;
            printf("%d %d %d \t %d\n",bitA,bitB,sum,carry);
        }
    }
    return 0;
}