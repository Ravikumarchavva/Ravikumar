#include <stdio.h>

void restoring_division(unsigned int dividend[], unsigned int divisor[], unsigned int *quotient, unsigned int *remainder) {
  unsigned int a = 0;
  unsigned int q = 0;
  int count = sizeof(dividend) * 8 - 1;
  printf("quo %u\n rem %u \n count %d \n",*quotient,*remainder,count);
}

int main() {
  unsigned int dividend[8],i ;
  unsigned int divisor[8];
  unsigned int quotient=0, remainder=0;
  for(i=0;i<8;i++){
    printf("%d ele",i+1);
    scanf("%u",&dividend[i]);
  }
  for(i=0;i<8;i++){
    printf("%d ele",i+1);
    scanf("%u",&divisor[i]);
  }
  for(i=0;i<8;i++){
    printf("%d",dividend[i]);
  }
  printf("\n");
  for(i=0;i<8;i++){
    printf("%d",divisor[i]);
  }
  printf("\n");
  restoring_division(dividend, divisor, &quotient, &remainder);

  printf("Quotient: %u\n", quotient);
  printf("Remainder: %u\n", remainder);

  return 0;
}
