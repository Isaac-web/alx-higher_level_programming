#!/usr/bin/node

const request = require('request');
const fs = require('fs');

function queryWebPage (url, file) {
  request.get({ url }, (err, response, body) => {
    fs.writeFile(file, body, { encoding: 'utf-8' }, (err) => {
      if (err) console.log(err);
    });
  });
}

const args = process.argv.slice(2);
queryWebPage(args[0], args[1]);
