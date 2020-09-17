#!/usr/bin/node

let arg = parseInt(process.argv[2]);
if (!isNaN(arg)) {
	for (let i = 0; i < arg; i++) {
		for (let j = 0; j < arg; j++) {
		  process.stdout.write('X');
	}
	console.log('');
  }
}
