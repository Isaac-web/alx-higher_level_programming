#!/usr/bin/node
const fs = require("fs");

function read_and_write(file, data) {
  fs.writeFile(file, data, { encoding: "utf-8" }, (err) => {
    if (err) console.log(err);
  });
}

const args = process.argv.slice(2);
read_and_write(args[0], args[1]);
