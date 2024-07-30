#!/usr/bin/node
const r = require('request');
const starwars = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${starwars}`;

r.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
