package main

import (
	"log"
	"net/http"
	"os"
)

func init() {
	log.SetFlags(log.LstdFlags | log.Lshortfile)
}

var portServiceMapping = map[string]string{
	"3001": "Service A",
	"3002": "Service B",
	"3003": "Service C",
	"3004": "Service D",
	"3005": "Service E",
	"3006": "Service F",
}

func main() {
	port := "3001"
	if len(os.Args) > 1 {
		port = os.Args[1]
	}

	handler := http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		w.WriteHeader(http.StatusOK)
		w.Write([]byte(portServiceMapping[port]))
	})

	mw := func(next http.Handler) http.Handler {
		return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
			log.Printf("Access: %v %v, Headers: %v\n", r.Method, r.URL.Path, r.Header)
			next.ServeHTTP(w, r)
		})
	}

	http.Handle("/", mw(handler))

	log.Println("Service started on", port)
	log.Fatal(http.ListenAndServe(":"+port, nil))
}
