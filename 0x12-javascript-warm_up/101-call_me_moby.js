#!/usr/bin/node
// function that executes x times a function.

exports.callMeMoby = function (i, theFunction) {
  for (let j = 0; j < i; j++) theFunction();
};
