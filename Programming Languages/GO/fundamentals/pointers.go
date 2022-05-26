// https://www.golang-book.com/books/intro/8
package main

import "fmt"

func var_changer(x *int) {
	// Assign new value to pointer x
	*x = 12

}

func main() {

	x := 5
	fmt.Printf("Variable X is --> %d\n", x)
	var_changer(&x) // Now values has changed
	fmt.Printf("Variable X is not --> %d\n", x)
}

// new

func pointer_func(x *int) {
	*x = 12
}

func main2() {
	x := new(int)
	fmt.Printf("X value --> %d | Memory Allocated --> %d\n", *x, x) // Nothing localted so should give the amount of memory allocated

	pointer_func(x) // with the new function we don't need to declare --> '&' before the function arguments

	fmt.Printf("X is not --> %d\n", *x) // Notice how to enter the value with need to reference is as a point

}
