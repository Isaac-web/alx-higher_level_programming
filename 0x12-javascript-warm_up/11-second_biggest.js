#!/usr/bin/node

const args = process.argv.slice(2).map((arg) => parseInt(arg));

if (args.length <= 1) {
  console.log(0);
} else {
  const maxIndex = args.findIndex((i) => i === Math.max.apply(null, args));
  args.splice(maxIndex, 1);
  const secondMax = Math.max.apply(null, args);
  console.log(secondMax);
}
