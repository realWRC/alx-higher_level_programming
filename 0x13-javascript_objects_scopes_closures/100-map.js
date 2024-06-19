#!/usr/bin/node
// script that imports an array and computes a new array

const list = require('./100-data').list;
const cpy = list.map((item, index) => item * index);
console.log(list);
console.log(cpy);
