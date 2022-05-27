/*

Installation

mkdir restful
cd restful

go mod init example/restful

// then

go get .
go run .

@credit: https://go.dev/doc/tutorial/web-service-gin

---------------------------
CURL COMMANDS
---------------------------

GET COMMAND

GET ALBUMS
curl http://localhost:8080/albums
GET Album by id
curl http://localhost:8080/albums/2

POST Albums
curl http://localhost:8080/albums     --include --header     "Content-Type: \
    application/json" --request     "POST" --data '{"id": "4","title": "The Modern Sound of Betty Carter","artist": "Betty Carter","price": 49.99}'


*/
package main

import (
	"fmt"
	"net/http"

	"github.com/gin-gonic/gin"
)

type album struct {
	ID     string  `json:"id"`
	Title  string  `json:"title"`
	Artist string  `json:"artist"`
	Price  float64 `json:"price"`
}

var albums = []album{
	{ID: "1", Title: "Blue Train", Artist: "John Coltrane", Price: 56.99},
	{ID: "2", Title: "Jeru", Artist: "Gerry Mulligan", Price: 17.99},
	{ID: "3", Title: "Sarah Vaughan and Clifford Brown", Artist: "Sarah Vaughan", Price: 39.99},
}

func main() {

	// Initialize the Router
	router := gin.Default()

	// ----------------------------
	// Routes
	// ----------------------------

	router.GET("/albums", getAlbums)
	router.GET("/albums/:id", getAlbumByID)
	router.POST("/albums", postAlbums)

	// start app
	router.Run("localhost:8080")

}

func getAlbums(c *gin.Context) {
	c.IndentedJSON(http.StatusOK, albums)
}

func postAlbums(c *gin.Context) {

	var newAlbum album

	if err := c.BindJSON(&newAlbum); err != nil {
		e := fmt.Sprintf("%v", err)
		c.IndentedJSON(http.StatusCreated, map[string]string{"hellow": e})
		return
	}

	albums = append(albums, newAlbum)
	c.IndentedJSON(http.StatusCreated, newAlbum)
}

func getAlbumByID(c *gin.Context) {
	id := c.Param("id")

	for _, a := range albums {
		if a.ID == id {
			c.IndentedJSON(http.StatusOK, a)
			return
		}
	}
	c.IndentedJSON(http.StatusNotFound, gin.H{"message": "album not found"})
}
