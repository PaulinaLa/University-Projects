
function fib(n)
{
if (n <= 1){
    return 1;
}
else{
    return fib(n-1) + fib(n-2);
}}

function fib_rec_time(n){
    console.time("timer_it");
    console.log(fib(n));
    console.timeEnd("timer_it");
}

console.log(fib_rec_time(7));

function fib_iter(n){
    console.time("timer_iter");
    var prev = 0;
    var acc = 1;
    var temp;
    while (n>1){
        temp = acc;
        acc = prev + acc;
        prev = temp;
        n--;
    }
    console.timeEnd("timer_iter");
    return acc;
}

console.log(fib_iter(8));