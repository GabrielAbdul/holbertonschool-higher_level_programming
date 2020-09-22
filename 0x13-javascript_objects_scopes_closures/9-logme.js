#!/usr/bin/node

let numPrintedArgs = 0;
exports.logMe = function (item) {
  console.log('$(numPrintedArgs++): $(item)');
};
