#include <stdio.h>

int main() {
    int n, a[100];

    printf("Nhap so phan tu: ");
    scanf("%d", &n);

    for(int i = 0; i < n; i++) {
        printf("a[%d] = ", i);
        scanf("%d", &a[i]);
    }

    for(int i = 0; i < n - 1; i++) {
        int max = i;

        for(int j = i + 1; j < n; j++) {
            if(a[j] > a[max]) {
                max = j;
            }
        }

        int temp = a[i];
        a[i] = a[max];
        a[max] = temp;

        printf("Buoc %d: ", i + 1);
        for(int k = 0; k < n; k++) {
            printf("%d ", a[k]);
        }
        printf("\n");
    }

    return 0;
}
