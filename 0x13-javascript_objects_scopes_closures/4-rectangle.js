#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print (character = 'X') {
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        process.stdout.write(character);
      }
      process.stdout.write('\n');
    }
  }

  rotate () {
    const temp_height = this.height;
    this.height = this.width;
    this.width = temp_height;
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }
};
