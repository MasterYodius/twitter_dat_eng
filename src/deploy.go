package main

import (
	"fmt"
	"log"
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

func main() {
	commandes1 := "docker build -t data-eng:latest ."
	commandes11 := "tree"
	commandes2 := "docker run --name PROJET -d -p 5000:5000 data-eng"
	tests := "conda run -n python37 python tests.py"
	commandes3 := "docker pause PROJET"
	commandes4 := "docker container rm --force PROJET"
	commandes5 := "docker image rm --force data-eng"
	commandes55 := "heroku login"
	commandes6 := "git add ."
	commandes7 := "git commit -m \"update\""
	commandes8 := "git push"
	commandes9 := "git push heroku HEAD:master"
	CMDcall(commandes11, true)
	CMDcall(commandes1, true)
	CMDcall(commandes2, true)
	_, err := CMDcall(tests, false)
	CMDcall(commandes3, true)
	CMDcall(commandes4, true)
	CMDcall(commandes5, true)
	if err == nil {
		fmt.Printf("Let's upload the git...")
		CMDcall(commandes55, true)
		CMDcall(commandes6, true)
		CMDcall(commandes7, true)
		fmt.Printf("Let's upload the github...")
		CMDcall(commandes8, true)
		fmt.Printf("Let's upload the heroku...")
		CMDcall(commandes9, false)
	}
}
