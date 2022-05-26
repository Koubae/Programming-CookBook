// https://go.dev/blog/maps
package main

import (
	"fmt"
	"sort"
)

func main() {

	m := make(map[int]string)
	m[1] = "hello"
	m[3] = "world"
	m[2] = "some"
	m[4] = "value"
	m[6] = "random"
	m[8] = "data"
	var keys []int
	for k := range m {
		keys = append(keys, k)
	}
	sort.Ints(keys)
	for _, k := range keys {
		fmt.Println("Key:", k, "Value:", m[k])
	}

}
