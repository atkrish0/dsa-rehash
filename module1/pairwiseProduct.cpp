#include<iostream>

int main() {
    int n;
    std::cin >> n;
    int a[n];
    for(int i = 0; i < n; i++) {
        std::cin >> a[i];
    }
    int maxProduct = 0;
    for(int i = 0; i < n; i++) {
        for(int j = i + 1; j < n; j++) {
            maxProduct = std::max(maxProduct, a[i] * a[j]);
        }
    }
    std::cout << maxProduct << std::endl;
    return 0;
}