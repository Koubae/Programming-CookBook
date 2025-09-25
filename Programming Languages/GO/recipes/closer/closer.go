package main

import (
	"fmt"
	"io"
	"log"
	"os"
)


func main() {
	f, err := os.Open("/tmp/test")
	if err != nil {
		log.Fatal(err)
	}
	defer closer(f)
	fmt.Println(f)

}

func closer(obj io.Closer) {
	err := obj.Close()
	if err != nil {
		log.Printf("Closer of type %T encountered an error while closing: %v\n", obj, err)
	}
}
