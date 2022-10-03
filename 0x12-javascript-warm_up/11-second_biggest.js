const args = process.argv.slice(2).map((arg) => parseInt(arg));

if (args.length <= 1) {
  return console.log(0);
} else {
  const max = Math.max.apply(null, args);
  console.log(max);
}
