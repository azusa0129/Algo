#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int n) {
    int answer = 0;
    while (true)
    {
        if (n == 0)
        {
            return answer;
        }
        answer += n % 10;
        n = n / 10;

    }
}