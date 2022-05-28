package main

import "fmt"

func main() {
	ch := make(chan int, 3)
	ch <- 1
	//ch <- 2
	//ch <- 10
	fmt.Println(<-ch)
	//fmt.Println(<-ch)
	//fmt.Println(<-ch)
}
