var express = require("express");
var app = express();

app.set('view engine', 'ejs');

app.get('/', (req, res) => {
    var value1 = 'Tutaj przekazuję wartość';
    var value2 = 'v2';
    res.render('zad2', {value1, value2});
});

app.listen(3000);
console.log('server started');