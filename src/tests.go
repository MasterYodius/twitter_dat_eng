package main

import (
	"bytes"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"os/exec"
	"strings"
)

//CMDcall sert à envoyer des commandes à la console
func CMDcall(commande string, debug bool) (string, error) {
	commandesplit := strings.Split(commande, " ")
	cmd := exec.Command(commandesplit[0], commandesplit[1:]...)
	out, err := cmd.CombinedOutput()
	fmt.Printf("combined out:\n%s\n", string(out))
	if (err != nil) && (debug == true) {
		log.Fatalf("cmd.Run() failed with %s\n", err)
	}
	return string(out), err
}

type reponse struct {
	statut bool
	data   string
}

func main() {
	responseBody := []byte("{\"phrase\": \"wall\"}")
	resp, err := http.Post("http://127.0.0.1:5000/RAM/", "json", bytes.NewBuffer(responseBody))
	fmt.Println(resp, err)
	body, _ := ioutil.ReadAll(resp.Body)
	//fmt.Println(body, err2)
	sb := string(body)
	fmt.Printf(sb)
	//regles à ajouter

}
