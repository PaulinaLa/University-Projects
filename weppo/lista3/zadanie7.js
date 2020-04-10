//zwykły iterator
function fib(){
    var f1 = 1, f2 = 1;
    return {
        next(){
            var current = f2;
            f2 = f1;
            f1 += current;
            return{
                value: current,
                done: false
            }
        }
    }
}
// df z yield - generator
function* nofib(){
    var n1 = 1, n2 = 1;
    while(true){
        let current = n2;
        n2 = n1;
        n1 += current;
        yield current;
    }

}

//tak można -> zwykłe wywołanie
// var _it = nofib();
// for (var _result; _result = _it.next(), !_result.done;){
//     console.log(_result.value);
// }



//iteratora nie da się tak wypisać -> zwróci błąd
// for(var i of fib()){ 
//     console.log(i);
// }



//tu się da jak jest generator
for (var i of nofib()){ 
    console.log(i);
}