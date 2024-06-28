#!/usr/bin/node
const x = process.argv.length;

console.log(x === 2? 'No argument': x ===3? "Argument found": "Arguments found");

// const y = process.argv.length;
// console.log(x > 2? "Argument" + (x>3? 's': '')+'found': 'No argument')