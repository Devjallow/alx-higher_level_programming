#!/usr/bin/node

const arg = process.argv.slice(2);
if (process.argv.length === 2) {
  console.log('Missing number of occurrences');
}
for (let i = 0; i < arg; i++) {
  console.log('C is fun');
}
