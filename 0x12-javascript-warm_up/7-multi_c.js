#!/usr/bin/node

const nan = isNaN(process.argv[2]);

if (nan === true) {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < process.argv[2]; i++) {
    console.log(process.argv[2]);
  }
}
