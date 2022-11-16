#!/usr/bin/node
const fs = require('fs');

function readAndWrite (file, data) {
  fs.writeFile(file, data, { encoding: 'utf-8' }, (err) => {
    if (err) console.log(err);
  });
}

const args = process.argv.slice(2);
readAndWrite(args[0], args[1]);
