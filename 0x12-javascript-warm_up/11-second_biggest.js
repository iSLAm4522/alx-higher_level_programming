#!/usr/bin/node
const { argv } = require('node:process');

const args = argv.slice(2).map(x => parseInt(x));

if (args.length < 2) {
  console.log(0);
} else {
  const arr = [...args];
  arr.sort((a, b) => b - a);
  console.log(arr[1]);
}
