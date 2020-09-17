#!/usr/bin/node
if (process.argv.legnth <= 3) {
	console.log('0');
} else {
	let num = process.argv.sort(function (a, b){return b-a})[3];
	console.log(num);
}
