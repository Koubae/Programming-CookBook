package main

import (
	"bufio"
	"context"
	"fmt"
	"io"
	"log"
	"net"
	"sync"
	"time"
)

// @docs https://pkg.go.dev/net
func main() {
	// host := net.JoinHostPort("localhost", "18000")
	// fmt.Println(host)

	SimpleServerClientEcho()
}

func SimpleTCPSocketGet() {
	conn, err := net.Dial("tcp", "golang.org:80")
	defer closeConn(conn)
	if err != nil {
		log.Fatal(err)
	}
	_, err = fmt.Fprintf(conn, "GET / HTTP/1.0\r\n\r\n")
	if err != nil {
		log.Fatal(err)
	}

	response, err := bufio.NewReader(conn).ReadString('\n')
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(response)
}

func SimpleTCPDealContext() {
	var d net.Dialer

	ctx, cancel := context.WithTimeout(context.Background(), 20*time.Second)
	defer cancel()

	conn, err := d.DialContext(ctx, "tcp", "golang.org:80")
	defer closeConn(conn)
	if err != nil {
		log.Fatal(err)
	}

	if _, err := conn.Write([]byte("GET / HTTP/1.0\n\n")); err != nil {
		log.Fatal(err)
	}

	response, err := bufio.NewReader(conn).ReadString('\n')
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(response)

}

func PrintAddr() {
	conn, err := net.Dial("tcp", net.JoinHostPort("golang.org", "80"))
	if err != nil {
		log.Fatal(err)
	}
	defer closeConn(conn)

	addr := conn.LocalAddr()
	fmt.Printf("Address: %s\n", addr)
}

func SimpleServerClientEcho() {
	const (
		TCPServerHost = "localhost"
		TCPServerPort = "18000"
		TotalClients  = 5
	)
	serverAddr := net.JoinHostPort(TCPServerHost, TCPServerPort)

	var wg sync.WaitGroup

	server := func(wg *sync.WaitGroup) {
		defer wg.Done()

		l, err := net.Listen("tcp", serverAddr)
		if err != nil {
			log.Fatal(err)
		}
		defer closeConn(l)

		log.Printf("{{SERVER}} Server started listening on %s\n", serverAddr)

		for {
			conn, err := l.Accept()
			if err != nil {
				log.Fatal(err)
			}

			log.Printf("{{SERVER}} New connection from %s\n", conn.RemoteAddr())

			go func(c net.Conn) {
				defer closeConn(c)
				_, err := io.Copy(c, c) // Echo incoming data
				if err != nil {
					log.Printf("{{SERVER}} Error while echoing data: %v\n", err)
				}
			}(conn)
		}

	}

	client := func(wg *sync.WaitGroup) {
		defer wg.Done()

		conn, err := net.Dial("tcp", serverAddr)
		if err != nil {
			log.Fatal(err)
		}
		defer closeConn(conn)

		log.Printf("{{CLIENT}} Connected to %s\n", serverAddr)

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

	time.Sleep(150 * time.Millisecond) // give server time to start

	for _ = range TotalClients {
		wg.Add(1)
		go client(&wg)
		time.Sleep(100 * time.Millisecond)
	}

	wg.Wait()

}

func closeConn(obj io.Closer) {
	err := obj.Close()
	if err != nil {
		log.Printf("Close Connection of type %T, error: %v\n", obj, err)
	}
}
