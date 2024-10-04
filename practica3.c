#include <stdio.h>
#include <time.h>

unsigned long long fibonacci(int n) {
    if (n <= 1) return n;
    return fibonacci(n - 1) + fibonacci(n - 2);
}

int main() {
    int n = 30; 
    for (int i = 1; i <= n; i++) {
        clock_t start = clock();
        unsigned long long fib = fibonacci(i);
        clock_t end = clock();
        double time_taken = ((double)(end - start)) / CLOCKS_PER_SEC * 1000; // Tiempo en ms
        printf("Fibonacci(%d) = %llu, Tiempo: %.5fms\n", i, fib, time_taken);
    }
    return 0;
}
