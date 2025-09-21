// my https://stackoverflow.com/a/79770821/13903942
package main

import (
	"bufio"
	"io"
	"log"
	"net"
	"sync"
	"time"
)

func main() {
	const (
		ServerHost = "127.0.0.1:8081"
		ClientHost = "127.0.0.1:8082"
	)
	addrServer, _ := net.ResolveTCPAddr("tcp", ServerHost)
	addrClient, _ := net.ResolveTCPAddr("tcp", ClientHost)

	var wg sync.WaitGroup

	server := func(wg *sync.WaitGroup) {
		defer wg.Done()
		listener, _ := net.ListenTCP("tcp", addrServer)
		log.Printf("{{SERVER}} listener addr: %s\n", listener.Addr().String())
		for {
			conn, err := listener.AcceptTCP()
			if err != nil {
				// handle error
				log.Fatal("err")
				return
			}

			// Handle connection func
			go func(conn *net.TCPConn) {
				defer conn.Close()
				log.Printf("{{SERVER}} conn addr: %s\n", conn.LocalAddr().String())
				log.Printf("{{SERVER}} conn remote addr: %s\n", conn.RemoteAddr().String())
				_, err := io.Copy(conn, conn) // Echo incoming data
				if err != nil {
					log.Printf("{{SERVER}} Error while echoing data: %v\n", err)
				}
			}(conn)
		}
	}

	client := func(wg *sync.WaitGroup) {
		defer wg.Done()

		// conn, err := net.Dial("tcp", host)
		conn, err := net.DialTCP("tcp", addrClient, addrServer)
		if err != nil {
			log.Fatal(err)
		}
		defer conn.Close()

		log.Printf("{{CLIENT}} (%s) Connected to %s\n", conn.LocalAddr().String(), conn.RemoteAddr().String())
		if _, err := conn.Write([]byte("Hello World\n")); err != nil {
			log.Fatal(err)
		}

		response, err := bufio.NewReader(conn).ReadString('\n')
		if err != nil {
			log.Fatal(err)
		}
		log.Printf("{{CLIENT}} Response: %s\n", response)

	}

	// Start Server
	wg.Add(1)
	go server(&wg)

	time.Sleep(150 * time.Millisecond) // Give some time for the server to start

	// Client Start
	wg.Add(1)
	go client(&wg)

	wg.Wait()

}
