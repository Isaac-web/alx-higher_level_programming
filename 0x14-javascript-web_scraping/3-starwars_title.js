#!/usr/bin/node
const request = require("request");

function getMovieTitle(id) {
  const url = `https://swapi-api.hbtn.io/api/films/${id}`;
  request({ url }, (err, response, body) => {
    if (err) return console.log(err);
    console.log(JSON.parse(body).title);
  });
}

const args = process.argv.slice(2);
getMovieTitle(args[0]);
