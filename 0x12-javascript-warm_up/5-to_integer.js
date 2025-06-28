#!/usr/bin/node
const { argv } = require('node:process');

const myNumber = parseInt(argv[2]);
console.log(`${isNaN(myNumber) ? 'Not a number' : `My number: ${myNumber}`}`);
