//różnice między operatorami typeof i instanceof
var example = 'to_zdecydowanie_string'


console.log(example instanceof String);
console.log(typeof example);

//Instanceof  sprawdza, czy dany obiekt jest instancją określonego typu 
//(konstruktora), czyli czy został utworzony przy pomocy konstruktora
//instanceof zwróci true, jeśli określony obiekt jest obiektem określonego typu

//typeof zwraca łańcuch zawierający typ operandu (łańcucha znaków, zmiennej, 
//słowa kluczowego lub obiektu).Operator typeof zwraca typ obiektu; sprawdza,
// czy dany obiekt jest typu prostego, czy jest czymkolwiek innym (obiektem).

var meal = new String('pizza'); 
console.log(meal instanceof String);
console.log(typeof pet1);

var desert = 'ice_cream';
console.log(desert instanceof String);
console.log(typeof desert);