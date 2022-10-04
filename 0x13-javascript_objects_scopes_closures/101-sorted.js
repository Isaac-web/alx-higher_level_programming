#!/usr/bin/node
const dict = require('./101-data.js').dict;

const obj = {};
for (let key in dict){
    if(!obj[dict[key]]){
        obj[dict[key]] = [];
        obj[dict[key]].push(key);
    }
    else{
        obj[dict[key]].push(key)
    }
}

console.log(obj);