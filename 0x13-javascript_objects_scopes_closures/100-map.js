#!/usr/bin/node
const list = require('./100data.js').list
console.log(list);
console.log(list.map((item, index) => item * index));
