#!/usr/bin/env bash
# takes in a URL, sends a request to that URL
# and displays the size of the body of the response
curl "$1" -sX POST -F "email: hr@holbertonschool.com" -F "subject: I will always be here for PLD"
