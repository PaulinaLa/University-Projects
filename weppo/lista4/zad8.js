const util = require('util');
const fs = require('fs');
const fsPromises = require('fs').promises;

//tak normalnie

fs.readFile('improwizacja.txt', 'utf-8', function(err, data) {
    console.log(data);
});


// funkcja ręczna
function funkcja_asynchroniczna(file_name, coding_type) {
    return new Promise(function(res, rej){
      fs.readFile(file_name, coding_type, function(err, data) {
        if (err) { rej(err); }
        res(data); 
      })
    });
}

funkcja_asynchroniczna("improwizacja.txt", "utf-8")
.then(function(text) {console.log(text);})
.catch(function(err) {console.log("ERROR", err);});

//po nowemu
async function funkcja_asyn_z_await() {
  try {
      const text = await funkcja_asynchroniczna("improwizacja.txt", {encoding: 'utf8'});
      console.log(text);
  }
  catch (err) {
      console.log('ERROR:', err);
  }
}

funkcja_asyn_z_await();



// z użyciem util.promisify   

const z_uzyciem_promisfy = util.promisify(fs.readFile);

z_uzyciem_promisfy("improwizacja.txt", "utf-8")
.then(function(text) {console.log(text);})
.catch(function(err) {console.log("ERROR", err);});

async function async_z_promisfy() {
  try {
      const text = await z_uzyciem_promisfy("improwizacja.txt", {encoding: 'utf8'});
      console.log(text);
  }
  catch (err) {
      console.log('ERROR:', err);
  }
}

async_z_promisfy();



// fs.promises 
const z_uzyciem_promises = fs.promises.readFile;

z_uzyciem_promises("improwizacja.txt", "utf-8")
.then(function(text) {console.log(text);})
.catch(function(err) {console.log("ERROR", err);});

async function async_z_promises() {
  try {
      const text = await z_uzyciem_promises("improwizajca.txt", {encoding: 'utf8'});
      console.log(text);
  }
  catch (err) {
      console.log('ERROR:', err);
  }
}

async_z_promises();