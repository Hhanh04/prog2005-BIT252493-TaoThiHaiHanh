
int main() {
    int i, j, isPrime;

    // In các số lẻ từ 111 đến 17 (giảm dần)
    printf("Cac so le tu 111 den 17 (giam dan):\n");
    for(i = 111; i >= 17; i--) {
        if(i % 2 != 0) {
            printf("%d ", i);
        }
    }
}
    // In các số nguyên tử  17 đến 111
    printf("\n\nCac so nguyen to tu 17 den 111:\n");
    for(i = 17; i <= 111; i++) {
        isPrime = 1;

        if(i > 1) {
            for(j = 2; j <= sqrt(i); j++) {
                if(i % j == 0) {
                    isPrime = 0;
                    break;
                }
            }
}
