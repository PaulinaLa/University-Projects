function fibrec(n){
    if (n == 0 || n == 1){
        return n
    }
    else{
        return fibrec(n-1) + fibrec(n-2);
    }
}

function memoize(fn) {

    let cache = {}

    return function(n){

        if (n in cache) {
            return cache[n]
        } else {
            let result = fn(n);
            cache[n] = result;
            return result
        }
    }
}

fibrec = memoize(fibrec);


function fibrec_time(n){
    console.time("timer_rec");
    console.log(fibrec(n));
    console.timeEnd("timer_rec");
}

function memoize_time(n) {
    console.log(fibrec(n));
    console.time("timer_mem");
    console.log(fibrec(n));
    console.timeEnd("timer_mem");
}

function summary(){
    for (var n = 10; n <= 40; n++){
        console.log("Czas rekurencyjnego dla n = " + n);
        console.log(fibrec_time(n));
        console.log("Czas memoizacji dla n = " + n);
        console.log(memoize_time(n));
    }
}

summary();