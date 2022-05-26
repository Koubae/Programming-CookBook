package main

import (
	"fmt"
	"sort"
)

func largest_range(array [12]int) [2]int {

	// 1) sort number in place
	sort.Ints(array[:])

	result_score := make(map[int][]int) // score , result mapping
	var scores []int                    // collection of scores
	var current_index = 0
	for {

		//res := make([]int, len(array)-current_index)

		var next_index int = current_index

		if next_index+1 > len(array) {
			break
		}

		var res []int
		var prev_value int = array[current_index]
		var initial_value int = prev_value // Store the initial value
		for _, value := range array[current_index:] {
			if value != initial_value && value != prev_value+1 {
				break
			}

			current_index += 1
			prev_value = value
			res = append(res, value)

		}
		// results = append(results, res)
		scores = append(scores, len(res))
		result_score[len(res)] = res

	}

	// now we get the largest score at the top
	sort.Sort(sort.Reverse(sort.IntSlice(scores)))

	// Get the higest score
	var score_winner = scores[0]
	// Get the result by the score_winner key
	res, _ := result_score[score_winner]

	fmt.Printf("Result --> %v\n", res)
	largest_range := [2]int{res[0], res[len(res)-1]}
	return largest_range
}

func algo_largest_range() {
	// Returns the largest (or longest) range of an array of subsequent integers.
	// The return value is an array of 2 integers of the range smalest, bigger and asume that the list contains only
	// one largest number

	// Example [2, 3, 4, 5, 6] -> [2, 6] | [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6] -> ??

	input := [12]int{1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6}
	var result [2]int = largest_range(input)
	fmt.Println(result)

}

func main() {

	algo_largest_range()
}
