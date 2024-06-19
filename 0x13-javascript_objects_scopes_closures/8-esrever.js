#!/usr/bin/node
// function that returns the reversed version of a list

exports.esrever = function (list) {
  const cpy = [];
  for (let i = list.length - 1; i >= 0; i--) {
    cpy.push(list[i]);
  }
  return cpy;
};
