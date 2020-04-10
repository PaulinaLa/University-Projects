var express = require('express');
var http = require('http');
var cookieParser = require('cookie-parser');
var url = require('url');
var bodyparser = require('body-parser');
var session = require('express-session');
var FileStore = require('session-file-store')(session);

function initDictEncode(dict) {
    var text = ""
    for (const d in dict) {
        text = text + '+' + dict[d].toString();
    }
    text=text.slice(1)
    console.log(text)
    return text
};

function intDictDecode(str) {
    var text = ""
    var dict = {}
    var num = 1
    console.log(str);
    for (const s in str) {
        if (str[s] != '+') {
            text += str[s];
        }
        else {
            dict[num] = parseInt(text);
            text = '';
            num += 1;
        }
    }
    if (text!='') {
        dict[num] = parseInt(text);
    }
    return dict
};

var app = express();

app.set('view engine', 'ejs');
app.set('views', './views');
app.use(cookieParser());
app.use(bodyparser.urlencoded({ extended: true}));
app.use(express.urlencoded({extended: true}));
app.use('/sessions', session({
    secret: 'keyboard cat',
    store: new FileStore,
    resave: false,
    saveUninitialized: true,
    cookieParser: { maxAge: 1000 * 60}
}))



app.get('/', (req, res) => {
    res.render('deklaracja');
});

app.post('/', (req, res) => {
    var name = req.body.name;
    var lecture = req.body.lecture;
    var date = req.body.date;
    var punkty = {
        1: req.body.zad1,
        2: req.body.zad2,
        3: req.body.zad3,
        4: req.body.zad4,
        5: req.body.zad5,
        6: req.body.zad6,
        7: req.body.zad7,
        8: req.body.zad8,
        9: req.body.zad9,
        10 :req.body.zad10,
    };
    for (var p in punkty) {
        if (punkty[p] == ''){
            punkty[p] = 0;
        }
    }
    res.redirect(
        url.format({
            pathname: "print",
            query: {
                name: name,
                lecture: lecture,
                punkty: initDictEncode(punkty),
                date: date,
            }
        })
    );
});

app.get('/print', (req, res) => {
    var punkty = intDictDecode(req.query.punkty);
    var model = req.query;
    model.punkty = punkty;
    console.log(punkty)
    res.render('print', model);
});

var server = http.createServer(app);
server.listen(3000);
console.log('started');