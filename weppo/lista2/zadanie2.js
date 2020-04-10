const pizza = {
    toppings: ['cheese', 'sauce', 'pepperoni'],
    crust: 'deep dish',
    serves: 2
  }


  const spaghetti = {
      ingredients: ['tomato_sauce', 'pasta', 'meat'],
      serving: 'dinner',
      portions: 20
  }

  console.log(pizza.crust);
  console.log(pizza["crust"]);

  //różnica polega na tym, że w przypadku [] można je 
  //stosować gdy w nazwie klucza występują znaki, których
  //nie można używać w nazwach zmiennych.

  console.log(pizza[3]);
  pizza[spaghetti] = 1;
  console.log(pizza[spaghetti]);



  //undefined

  pizza[3] = 33;
  pizza[spaghetti] = 'lasagne';

  console.log(pizza);

  var tab = ['pepperoni', 'salami', 'mozarella'];

console.log(tab["2"]);
console.log(tab[pizza]);
tab ['guacamole'] = 'mexican_fiesta';
console.log(tab);

console.log(tab.length);

tab.length = 70;

console.log(tab.length);
console.log(tab);

tab.length = 2;

console.log(tab.length);
console.log(tab);





  console.log(pizza[tab]);

  pizza[tab] = 'toppings2';


