#include <stdio.h>

int main() {
    int n, i, j;

    printf("Nhap n: ");
    scanf("%d", &n);

    // Hinh 1
    printf("Hinh 1:\n");
    for(i = 1; i <= n; i++) {
        for(j = 1; j <= i; j++) {
            printf("%d ", j);
        }
        printf("\n");
    }

    // Hinh 2
    printf("Hinh 2:\n");
    for(i = 1; i <= n; i++) {

        // in khoang trang
        for(j = 1; j <= n - i; j++) {
            printf(" ");
        }

        // in dau *
        for(j = 1; j <= 2*i - 1; j++) {
            if(i == 1 || i == n || j == 1 || j == 2*i - 1)
                printf("*");
            else
                printf(" ");
        }

        printf("\n");
    }

    return 0;
}
