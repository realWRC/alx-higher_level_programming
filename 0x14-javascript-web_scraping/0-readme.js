#!/usr/bin/node

const fs = require('fs');
const file = process.argv[2];

fs.readFile(file, 'utf-8', (err, info) => {
  if (err) {
    console.log(err);
  } else {
    console.log(info);
  }
});
