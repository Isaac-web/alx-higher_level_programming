#!/usr/bin/node
const fs = require('fs');
function readAndPrint (file) {
  fs.readFile(file, 'utf-8', (err, data) => {
    if (err) return console.log(err);

    console.log(data);
  });
}

const args = process.argv.slice(2);
readAndPrint(args[0]);
