#!/usr/bin/node
const { argv } = require('node:process');
const num = parseInt(argv[2]);

function factorial (n) {
  if (isNaN(n) || n === 0) {
    return 1;
  }
  return n * factorial(n - 1);
}

console.log(factorial(num));
