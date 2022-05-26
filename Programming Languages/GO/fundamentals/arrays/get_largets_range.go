package main

import (
	"fmt"
	"sort"
)

func largest_range(array [12]int) [2]int {
	sort.Ints(array[:]) // sort number in plase

	var result [2]int
	result[0] = array[0]
	result[1] = array[len(array)-1]
	return result
}

func main() {

	input := [12]int{1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6}
	var result [2]int = largest_range(input)
	fmt.Println(result)
}

// or also
/*
package main

import (
	"fmt"
	"sort"
)
*/

func largest_range(array [12]int) [2]int {
	sort.Ints(array[:]) // sort number in plase

	result := [2]int{array[0], array[len(array)-1]}
	return result
}

func main() {

	input := [12]int{1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6}
	var result [2]int = largest_range(input)
	fmt.Println(result)
}
