var pgpromise = require('pg-promise')(/* options */)
var data_base = pgpromise('postgres://postgres:1234@localhost/lista8')



async function idOsoby(nazwa){
    return data_base.task('idOsoby', async t => {
        const nr_osoby = await t.oneOrNone('SELECT id FROM zad2 WHERE nazwa = $1', nazwa, u => u && u.id);
        return nr_osoby || await t.one('INSERT INTO zad2(nazwa) VALUES($1) RETURNING id', nazwa, u => u.id);
    });
}

async function pobierz_dane(){
    return data_base.task('pobierz_dane', async t => {
        const users = await t.any('SELECT * FROM zad2');
        return users;
    });
}

function zwroc_dane(){
    pobierz_dane().then( data => console.log(data)).catch( err => console.log(err));
}

idOsoby('Zdzisław').then(userId => {
    console.log('id tej osoby to:', userId)
})
.catch(error => {});

zwroc_dane();

data_base.$pool.end()