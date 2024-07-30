#!/usr/bin/node
const fs = require('fs');
const file = process.argv[2];
const data = process.argv[3];

function writer (file, data) {
  fs.writeFile(file, data, function (err) {
    if (err) {
      console.log(err);
    }
  });
}
writer(file, data);
