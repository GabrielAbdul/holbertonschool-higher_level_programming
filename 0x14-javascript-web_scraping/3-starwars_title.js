#!/usr/bin/node

movieId = process.argv[2];
endPoint = 'https://swapi-api.hbtn.io/api/films/' + movieId

const request = require('request');

request(endPoint, (err, res, body) => {
	if (err) { console.log(err); };
	let jsonRespone = JSON.parse(body);
	console.log(jsonRespone.title);
});
