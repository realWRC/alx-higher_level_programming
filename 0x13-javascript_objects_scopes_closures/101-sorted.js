#!/usr/bin/node
// script that imports a dictionary of occurrences by user id and computes a dictionary
// of user ids by occurrences

const dict = require('./101-data.js').dict;

const cpy = {};
for (const key in dict) {
  if (cpy[dict[key]] === undefined) {
    cpy[dict[key]] = [key];
  } else {
    cpy[dict[key]].push(key);
  }
}
console.log(cpy);
