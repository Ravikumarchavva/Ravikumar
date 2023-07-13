#include <stdio.h>

void decimalToBinary(int decimal) {
    // Determine the number of bits required to represent the decimal number
    int numBits = sizeof(decimal) * 8;
    printf("%d\n", numBits);
    // Create a mask to extract the most significant bit
    int mask = 1 << (numBits - 1);
    printf("%d\n", mask);
    // Print the binary representation
    printf("Binary: ");
    
    for (int i = 0; i < numBits; i++) {
        // Use bitwise AND to extract the current bit
        int bit = (decimal & mask) != 0;
        
        // Print the current bit
        printf("%d", bit);
        
        // Shift the mask to the right for the next bit
        mask >>= 1;
    }
    
    printf("\n");
}

int main() {
    int decimal = 42;
    
    printf("Decimal: %d\n", decimal);
    
    decimalToBinary(decimal);
    
    return 0;
}
