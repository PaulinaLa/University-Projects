var Foo = function (value){
    this.value = value;
}

Foo.prototype.Bar = (function(){
    function Qux(){
        console.log("PRYWATNA");
    }

    return function() {
        return console.log("PUBLICZNA") + Qux()
    }})();

var test = new Foo('testowy string');
console.log(test.value);
console.log(test.Bar());