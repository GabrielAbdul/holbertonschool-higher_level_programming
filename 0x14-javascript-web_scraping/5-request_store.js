#!/usr/bin/node

const request = require('request');
const fs = require('fs');
let endPoint = process.argv[2];
let filePath = process.argv[3];
request(endPoint, (err, res, body) => {
	if (err) { console.log(err); };
	let stringToWrite = body;
	fs.writeFile(filePath, stringToWrite, 'utf8', (err) => {
	if (err) { console.log(err); return; };
});
	});

