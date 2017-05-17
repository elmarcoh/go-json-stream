package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
)

func main() {
	resp, err := http.Get("http://localhost:8000/stream")
	dec := json.NewDecoder(resp.Body)

	for dec.More() {
		var m map[string]string
		if err = dec.Decode(&m); err != nil {
			log.Fatal(err.Error())
		}
		fmt.Printf("got message %+v\n", m)
	}
}
