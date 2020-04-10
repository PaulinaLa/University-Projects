var a = [1,2,3,4];

function forEach (a, f){
    for (let i = 0; i < a.length; i++){
        a[i] = f(a[i]);
    }
    return a;
}

function fac(n){
    return n*n;
}

function is_even(n){
    return n % 2 == 0;
}

console.log(forEach(a, fac));
forEach(a, _ => {console.log( _ );});

list = [1,2,3,4,5,6];

function map (a, f){
    let re = [a.length];
    for (let i = 0; i < a.length; i++){
        re[i] = f(a[i]);
    }
    return re;
}

console.log(map(list, fac));
console.log(list);

console.log(map(list, _ => _ * 2));


function filter(arr, filterFunc){    
    const filterArr = [];    
    for(let i=0;i<arr.length;i++) {   
        const result = filterFunc(arr[i], i, arr);       
        if(result){       
            filterArr.push(arr[i]);
        }   
    }
    return filterArr;
}

console.log(list);
var a = [1,2,3,4];
console.log(filter(a , _ => _ < 3));
console.log(filter(a, is_even));

