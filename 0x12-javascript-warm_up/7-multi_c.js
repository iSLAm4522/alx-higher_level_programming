#!/usr/bin/node
const { argv } = require('node:process');
const str = 'C is fun';
let times = parseInt(argv[2]);

if (isNaN(times)) { console.log('Missing number of occurrences'); } else {
  while (times-- > 0) { console.log(str); }
}
