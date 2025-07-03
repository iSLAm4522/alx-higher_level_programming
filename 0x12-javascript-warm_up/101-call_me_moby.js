#!/usr/bin/node

function callMeMoby (x, callbckfun) {
  while (x--) { callbckfun(); }
}

module.exports = { callMeMoby };
