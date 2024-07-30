#!/usr/bin/node
const r = require('request');
const fs = require('fs');

r(process.argv[2], function (_err, _response, body) {
  fs.writeFile(process.argv[3], body, 'utf8', function (err) {
    if (err) {
      console.log(err);
    }
  });
});
