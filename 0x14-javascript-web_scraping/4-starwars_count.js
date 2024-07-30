#!/usr/bin/node
const r = require('request');
const url = process.argv[2];
const charID = '18';
let numb = 0;

r.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body);
    data.results.forEach((film) => {
      film.characters.forEach((character) => {
        if (character.includes(charID)) {
          numb += 1;
        }
      });
    });
    console.log(numb);
  }
});
