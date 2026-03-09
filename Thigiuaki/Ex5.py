#include <stdio.h>

void bai1() {
    printf("Dang chay Bai 1...\n");
}

void bai2() {
    printf("Dang chay Bai 2...\n");
}

void bai3() {
    printf("Dang chay Bai 3...\n");
}

void bai4() {
    printf("Dang chay Bai 4...\n");
}

int main() {
    int choice;

    do {
        printf("\n===== MENU =====\n");
        printf("1. Bai 1\n");
        printf("2. Bai 2\n");
        printf("3. Bai 3\n");
        printf("4. Bai 4\n");
        printf("0. Thoat\n");
        printf("Chon chuong trinh: ");
        scanf("%d", &choice);

        switch(choice) {
            case 1:
                bai1();
                break;
            case 2:
                bai2();
                break;
            case 3:
                bai3();
                break;
            case 4:
                bai4();
                break;
            case 0:
                printf("Thoat chuong trinh!\n");
                break;
            default:
                printf("Lua chon khong hop le!\n");
        }

    } while(choice != 0);

    return 0;
}

