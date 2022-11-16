const request = require('request');

function printStatusCode (url) {
  request.get({ url }, (err, response, body) => {
    if (err) return console.log(err);
    console.log(`code: ${response.statusCode}`);
  });
}

const args = process.argv.slice(2);
printStatusCode(args[0]);
