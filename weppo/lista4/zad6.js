var fs = require('fs');
var filename = 'improwizacja.txt';

function czytaj(){
    fs.readFile(filename, 'utf8', function(err, data) {
        if(err){
            throw err;
        }
        console.log(data);
    })};

czytaj();