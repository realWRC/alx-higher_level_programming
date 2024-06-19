#!/usr/bin/node
// function that returns the number of occurrences in a list.

exports.nbOccurences = function (list, searchElement) {
  let ocr = 0;
  for (const element of list) {
    if (element === searchElement) {
      ocr++;
    }
  }
  return ocr;
};
