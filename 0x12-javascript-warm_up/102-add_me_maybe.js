#!/usr/bin/node

function addMeMaybe (value, callbackfun) {
  value++;
  callbackfun(value);
}

module.exports = { addMeMaybe };
