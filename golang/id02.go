package main

import "fmt"

type Known struct {
    value map[int]int
}

func fib(n int) int {
    Known.value[0] = 0
    Known.value[1] = 1
    if val, ok := Known[n]; ok {
        return val
    } else {
        answer := fib(n-1) + fib(n-2)
        Known[n] = answer
        return answer
    }
}

func main() {
    total := 0
    for i := 0; fib(i) < 4000000; i++ {
        if fib(i) % 2 == 0 {
            total += fib(i)
        }
    }
    fmt.Println(total)
}
