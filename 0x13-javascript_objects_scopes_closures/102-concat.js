#!/usr/bin/node
const fs = require('fs');

const fArg = fs.readFileSync(process.argv[2]).toString();
const sArg = fs.readFileSync(process.argv[3]).toString();
fs.writefileSync(process.argv[4], fArg + sArg);
