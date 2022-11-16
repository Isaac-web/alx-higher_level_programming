#!/usr/bin/node
const request = require('request');

function verifyMovie (characters) {
  const result = characters.filter((c) => c.endsWith('18/'));
  return result.length ? true : false;
}

function printMovieCount (url) {
  request.get({ url }, (err, response, body) => {
    let results = JSON.parse(body).results;
    results = results.map((r) => r.characters);
    results = results.filter((r) => verifyMovie(r) == true);
    console.log(results.length);
  });
}

const args = process.argv.slice(2);
printMovieCount(args[0]);
