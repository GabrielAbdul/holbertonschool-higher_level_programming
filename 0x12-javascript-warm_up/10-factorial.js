#!/usr/bin/node

arg = process.argv[2];
isNaN(arg) ? console.log(1) : console.log(factorial(arg));

function factorial (a) {
  if (a <= 1) {
	  return 1
  }
  return a * factorial(a - 1);
}
