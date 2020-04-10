var express = require('express');
var app = express();
var fs = require('fs');
var {promisify} = require('util');
var multer = require('multer');
var upload = multer({ storage: multer.diskStorage({
  destination: (req, res, cb) => {
    cb(null, './pobrane');
  },
  filename: (req, file, cb) => {
    cb(null, file.originalname);
  }
})});

app.set('view engine', 'ejs');
app.use(express.static(__dirname + '/pobrane'));
var readdir = promisify(fs.readdir);

app.get('/', async (req, res) => {
  try {
    const nazwy = await readdir('./pobrane/', );
    res.render('index', {nazwy});
  } catch (e) {
    console.error(e);
    res.send('something went wrong:', e);
  }
  
})

app.post('/', upload.single('file'), (req, res) => {
  res.redirect('/');
})

app.listen(3000);
console.log('server start');