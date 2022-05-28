package main

import "fmt"

func fibonacciCalc() func() int {
	var nth = 0
	var prevNum int = 0
	var currentNum int = 1
	return func() int {
		nth++
		var result int = prevNum + currentNum
		if nth != 1 {
			prevNum = currentNum
		}

		currentNum = result
		return result
	}
}

func main() {

	var fibonacciLimit int = 10
	fibonacci := fibonacciCalc()
	for i := 0; i < fibonacciLimit; i++ {
		fmt.Println(fibonacci())
	}
}
