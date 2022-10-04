#!/usr/bin/node

const ParentSquare = require("./5-square");

class Square extends ParentSquare{
    constructor(size){
        super(size);
    }

    charPrint(c){
        for(let i = 0; i < this.height; i++){
            let line = '';
            for(let j = 0; j < this.width; j++){
                line += c || 'X'
            }
            console.log(line);
        }
    }
}

module.exports = Square;