#!/usr/bin/node
// Definse empty class Square that defines a Square object.
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}
module.exports = Square;
