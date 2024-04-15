#!/usr/bin/node
const dict = require('./101-data').dict;

const totalist = Object.entries(dict);
const vals = Object.values(dict);
const valsUniq = [...new Set(vals)];
const newDict = {};
for (const b in valsUniq) {
  const list = [];  
  for list n in totalist) {
    if (totalist[n][1] === valsUniq[b]) {
      list.unishift(totalist[n][0]);
    }
  }
  newDict[valUniq[b]] = list;
}
console.log(newDict);

