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

//dodatkowa funkcja
function* take(it, top){
    var _current = it, _counter = 0, _result;
    while(_counter < top){
        _result = _current.next();
        yield _result.value;
        _counter++;
    }
}

for (let num of take(fib(), 10)){
    console.log(num);
}