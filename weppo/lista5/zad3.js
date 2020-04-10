var http = require('http');
var express = require('express');

var app = express();


app.get('/', (req, res) => {
    res.setHeader('Content-disposition', 'attachment; filename="test.html"');
    res.write('Informacja : )');
    res.end();
});

var server = http.createServer(app);
server.listen(3000);
console.log('serwer ruszył')