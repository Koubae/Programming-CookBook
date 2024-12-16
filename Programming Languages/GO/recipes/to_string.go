package main

import "fmt"

type Person struct {
	Name string
	Age  int
}

func (p Person) String() string {
	return fmt.Sprintf("name=%s, age=%d", p.Name, p.Age)
}

func main() {
	john := Person{"John", 42}
	mark := Person{"Mark", 24}

	fmt.Println(john)
	fmt.Println(mark)
}
