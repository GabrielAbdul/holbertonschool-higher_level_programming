#!/usr/bin/node

const Rectangle = require('./5-square');
module.exports = class Square extends Rectangle {
  charPrint (c) {
    if (!c) {
      return super.print();
    } else {
      return super.print('C');
    }
  }
};
