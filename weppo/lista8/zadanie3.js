var pgpromise = require('pg-promise')(/* options */)
var data_base = pgpromise('postgres://postgres:1234@localhost/lista8')

async function update_data(id, nowe) {
    data_base.task('update_data', async t => {
        await t.oneOrNone('UPDATE zad2 SET nazwa = $2 WHERE id = $1', [id, nowe]);
    });
}

async function delete_data(id) {
    data_base.task('delete_data', async t => {
        await t.oneOrNone('DELETE FROM zad2 WHERE id = $1', id);
    });
}

update_data(2, 'Salomon');
delete_data(1);

data_base.$pool.end()