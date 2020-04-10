var pgpromise = require('pg-promise')(/* options */)
var db = pgpromise('postgres://postgres:1234@localhost/lista8')

// async function clear() {
//     return db.task('clear', async t => {
//       let counter = await t.result('DELETE FROM osoby', null, a => a.rowCount);
//        return counter + await t.result('DELETE FROM miejsca_pracy', null, a => a.rowCount);
//     });
//   }
  
  async function dodaj(osoba, miejsce) {
    return db.task('dodaj', async t => {
      let obiekt_miejsca = await t.oneOrNone('SELECT id FROM miejsca_pracy WHERE nazwa = $1', miejsce.nazwa);
      const id_miejsca = obiekt_miejsca ?
      obiekt_miejsca.id : 
       await t.one('INSERT INTO miejsca_pracy(nazwa) VALUES($1) RETURNING id', miejsce.nazwa, w => w.id );
      return await t.none('INSERT INTO osoby(nazwa, miejsca_pracy_id) VALUES($1, $2)', [osoba.nazwa, id_miejsca])
    });
  }
  
  async function zwroc_dane() {
    return db.task('zwroc_dane', async t => {
      const osoby = await t.any('SELECT * FROM osoby');
      for (const osoba of osoby) {
        const miejsce = await t.one('SELECT * FROM miejsca_pracy WHERE id = $1', osoba.miejsca_pracy_id);
        console.log('osoba:', osoba, 'miejsce pracy:', miejsce);
      }
    })
  }
  
const person = { nazwa: 'Mateusz Bulanda' };
const workplace = { nazwa: 'Orlen' };
dodaj(person, workplace).then( res => {
    zwroc_dane();
});

