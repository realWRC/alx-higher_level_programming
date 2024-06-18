#!/usr/bin/node
// script that searches the second biggest integer in the logs of arguments

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const logs = process.argv.sort();
  console.log(logs.reverse()[1]);
}
