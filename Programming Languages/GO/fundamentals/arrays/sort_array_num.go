package main

import (
	"fmt"
	"sort"
)

func largest_range(array [12]int) [12]int {
	sort.Ints(array[:]) // sort number in plase
	return array
}

func main() {

	input := [12]int{1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6}
	var result [12]int = largest_range(input)
	fmt.Println(result)
}

// [0 1 2 3 4 5 6 7 10 11 12 15]
