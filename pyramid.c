#include <stdio.h>
void printPyramid(int height) {
    for (int i = 1; i <= height; i++) {
        for (int j = i; j < height; j++) {
            printf(" ");
        }
        for (int k = 1; k <= (2 * i - 1); k++) {
            printf("*");
        }
        printf("\n");
    }
}
int main() {
    int height;
    printf("Enter the height of the pyramid: ");
    scanf("%d", &height);
    printPyramid(height);
    return 0;
}
