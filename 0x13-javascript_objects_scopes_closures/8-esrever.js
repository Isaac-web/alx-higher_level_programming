#!/usr/bin/node

exports.esrever = function (list) {
  const rev = [];

  list.forEach((item, index) => {
    rev[list.length - (index + 1)] = item;
  });

  return rev;
};
