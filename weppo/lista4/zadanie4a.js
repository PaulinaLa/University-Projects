function Module1() {
}

module.exports = Module1;

var module2 = require('./zadanie4b');

Module1.show = function() {
    console.log("Moduł 1 się zgłasza!");
};