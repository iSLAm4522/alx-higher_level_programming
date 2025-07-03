#!/usr/bin/node

function callMeMoby (x, callbckfun) {
  while (x-- > 0) { callbckfun(); }
}

module.exports = { callMeMoby };
