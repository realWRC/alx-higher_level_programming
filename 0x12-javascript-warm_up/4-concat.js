#!/usr/bin/node
// script that prints two arguments passed to it, in the following format: “ is ”
const arg0 = process.argv[2];
const arg1 = process.argv[3];
console.log(`${arg0} is ${arg1}`);
