#!/usr/bin/node
const { argv } = require('node:process');
const size = parseInt(argv[2]); let cnt = 0; let str = '';
if (isNaN(size)) { console.log('Missing size'); }

while (cnt++ < size) { str += 'X'; }

cnt = 0;

while (cnt++ < size) { console.log(str); }
