#!/usr/bin/node
const { argv } = require('node:process');

const result = argv[2] ? argv[2] : 'No argument';
console.log(result);
