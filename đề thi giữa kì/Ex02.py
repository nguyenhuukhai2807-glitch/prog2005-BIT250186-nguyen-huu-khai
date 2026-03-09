#include <stdio.h>
#include <math.h>

int main() {
    float a, b, c;
    float max, min;
    float delta, x1, x2;

    // Nhập a, b, c
    printf("Nhap a, b, c: ");
    scanf("%f %f %f", &a, &b, &c);

    // Tìm số lớn nhất
    max = a;
    if (b > max) max = b;
    if (c > max) max = c;

    // Tìm số nhỏ nhất
    min = a;
    if (b < min) min = b;
    if (c < min) min = c;

    printf("So lon nhat: %.2f\n", max);
    printf("So nho nhat: %.2f\n", min);

    // Giải phương trình bậc hai
    if (a == 0) {
        if (b == 0) {
            if (c == 0)
                printf("Phuong trinh vo so nghiem\n");
            else
                printf("Phuong trinh vo nghiem\n");
        } else {
            printf("Phuong trinh bac nhat, nghiem x = %.2f\n", -c/b);
        }
    } else {
        delta = b*b - 4*a*c;

        if (delta < 0) {
            printf("Phuong trinh vo nghiem\n");
        } else if (delta == 0) {
            printf("Phuong trinh co nghiem kep x = %.2f\n", -b/(2*a));
        } else {
            x1 = (-b + sqrt(delta))/(2*a);
            x2 = (-b - sqrt(delta))/(2*a);
            printf("x1 = %.2f\n", x1);
            printf("x2 = %.2f\n", x2);
        }
    }

    return 0;
}

