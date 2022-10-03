#!/usr/bin/node

const numberOfPrints = parseInt(process.argv[2]);

if (!numberOfPrints) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < numberOfPrints; i++) {
    console.log('C is fun');
  }
}
