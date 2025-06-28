#!/usr/bin/node
const { argv } = require('node:process');

const myNumber = parseInt(argv[2]);
console.log(`My number: ${isNaN(myNumber) ? 'Not a number' : myNumber}`);
