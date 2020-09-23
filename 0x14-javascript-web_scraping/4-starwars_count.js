#!/usr/bin/node

const request = require('request');
let endPoint = process.argv[2];
let numMoviesWedgeIn = 0;
request(endPoint, (err, res, body) => {
	if (err) { console.log(err); };
	let jsonResponse = JSON.parse(body);
	for (let i = 0; i < jsonResponse.results.length; i++) {
		for (let j = 0; j < jsonResponse.results[i].characters.length; j++) {
			if (jsonResponse.results[i].characters[j].includes('18')) { numMoviesWedgeIn++ };
		}
	}
	console.log(numMoviesWedgeIn);
});
