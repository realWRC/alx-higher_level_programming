#!/usr/bin/node
// Definse empty class Square that defines a Square object.
const superSquare = require('./5-square');

class Square extends superSquare {
  charPrint (c = 'X') {
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}
module.exports = Square;
