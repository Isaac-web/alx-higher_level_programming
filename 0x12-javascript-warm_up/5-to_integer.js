#!/usr/bin/node

let firstNumber = parseInt(process.argv[2]);

if (!firstNumber) console.log("Not a number");
else console.log("My number is: " + firstNumber);
