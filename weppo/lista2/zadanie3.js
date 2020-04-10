console.log( (![]+[])[+[]]+(![]+[])[+!+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]] );

console.log([]); // []
console.log(![]) // false
console.log((![]+[])); //false string
console.log([+[]]); // [0]
console.log((![]+[])[+[]]); // = false[0]
console.log([+!+[]]);// [1]
console.log((![]+[])[+!+[]]);//a
console.log( (![]+[])[+[]]+(![]+[])[+!+[]]); // fa
console.log(([![]]+[][[]]))//falseundefined
console.log([][[]]); // undefined
console.log([+!+[]+[+[]]]);// ['10']
console.log([!+[]+!+[]]); //[2]
