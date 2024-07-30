#!/usr/bin/node
const r = require('request');
const star_wars = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${star_wars}`;

r.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
