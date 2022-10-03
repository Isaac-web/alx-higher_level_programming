#!/usr/bin/node
const firstNumber = parseInt(process.argv[2]);
if (firstNumber === NaN) console.log('Not a number');
else console.log('My number is: ' + firstNumber);
