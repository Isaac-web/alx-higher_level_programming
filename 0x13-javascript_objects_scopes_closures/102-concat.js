const fs = require('fs');

const args = process.argv.slice(2);

args.forEach(filePath =>
  fs.readFile(`./${filePath}`, 'utf8', (err, data) => {
    if (err) console.error(err);
    console.log(data);
  }));
