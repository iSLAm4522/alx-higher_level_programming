#!/usr/bin/node

function addMeMaybec (value, callbackfun) {
  value++;
  callbackfun(value);
}

module.exports = { addMeMaybec };
