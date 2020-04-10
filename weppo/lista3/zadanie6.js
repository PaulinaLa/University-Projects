function createGenerator(parametr){ //zastąpienie 10 przez parametr
    return function(){
        var _state = 0;
        return {
            next: function(){
                return{
                    value: _state,
                    done: _state++ >= parametr
                }
            }
    }   }   
}

function upto(param){ //wywoływanie do pewnego parametru
    return{
        [Symbol.iterator]: createGenerator(param)
    }
}

var foo1 = upto(50); 
var foo2 = upto(100);

for (var f of foo1){
    console.log(f);
}

for (var g of foo2){
    console.log(g);
}