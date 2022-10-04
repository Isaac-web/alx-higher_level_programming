#!/usr/bin/node

class Rectangle{
    constructor(w, h){
        if(w > 0 && h > 0){
            this.height = h;
            this.width = w;
        }
    }

    double(){
        this.height*=2;
        this.width*=2;
    }


    print(){
        for(let i = 0; i < this.height; i++){
            let line = '';
            for(let j = 0; j < this.width; j++){
                line += 'X';
            }
            console.log(line);
        }
    }

    rotate(){
        this.height ^= this.width;
        this.width ^= this.height;
        this.height ^= this.width;
    }
}

module.exports = Rectangle;