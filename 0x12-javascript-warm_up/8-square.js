#!/usr/bin/node
// script that prints a square

const size = process.argv[2];

if (!parseInt(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    let j = 0;
    let delin = '';

    while (j < size) {
      delin = delin + 'X';
      j++;
    }
    console.log(delin);
  }
}
