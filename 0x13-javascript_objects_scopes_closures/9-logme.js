#!/usr/bin/node

const numPrintedArgs = 0;
exports.logMe = function (item) {
  console.log('$(numPrintedArgs++): $(item)');
};
