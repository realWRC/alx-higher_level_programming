#!/usr/bin/node
const r = require('request');
const url = process.argv[2];

r.get(url, (err, response) => {
  if (err) {
    console.log(err);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
