

var test = {
    description: "hello",

    foocounter : 0,

    _starting : 4,

    details(){
        console.log(`Hi and ${this.description}`);
    },

    get bar() { // użycie akc. get
        return test._starting;
    },

    set bar(i){ //użycie akc. set
        console.log('using bar setter');
        test._starting = i;
    }
}

console.log(test);
console.log(test.details());

//jak dodać nowe pole
test['name'] = "John";
console.log(test);

Object.defineProperty(test, 'baz', {
    value : function(){
        return 17;
    }
});

console.log(test.baz());

Object.defineProperty(test, 'foo', {
    get foo(){
        return foocounter;
    }
})

Object.defineProperty(test, 'foo', {
    /**
     * @param {number} i
     */
    set foo(i){
        console.log('using setter');
        test.foocounter = i;
    }
})

test.bar = 15;
test.bar = 20;
console.log(test.bar);


