#!/bin/bash
# takes in a URL, sends a request to that URL and displays the size of the body of the response
curl "$1" -sH "X-HolbertonSchool-User-Id: 98"
