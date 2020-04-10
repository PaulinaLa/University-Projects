const readline = require('readline');
const fs = require('fs');

function najczestsze_elem(tab){
    let dict = {};
    let maxEl = tab[0];
    let counter = 1;

    for(let i = 0; i < tab.length; i++){
        let elem = tab[i];

        if(dict[elem] == null){
            dict[elem] = 1;
        }
        else{
            dict[elem]++;
        }
        if(dict[elem] > counter){
            maxEl = elem;
            counter = dict[elem];
        }
    }
    return maxEl;
}

function najczestsze_liczba(tab){
    let dict = {};
    let maxEl = tab[0];
    let counter = 1;

    for(let i = 0; i < tab.length; i++){
        let elem = tab[i];

        if(dict[elem] == null){
            dict[elem] = 1;
        }
        else{
            dict[elem]++;
        }
        if(dict[elem] > counter){
            maxEl = elem;
            counter = dict[elem];
        }
    }
    return dict[maxEl];
}

function usun(nums, val){
    for (let i = nums.length - 1; i >= 0; i--){
        if (nums[i] == val){
            nums.splice(i,1);
        }
    }
}


const rl = readline.createInterface({
    input: fs.createReadStream('logs.txt')});

let lista_logow = []
rl.on('line', (line) => {
    let str = line.split(" ")[1]
    lista_logow.push(str)});

rl.on('close', () => {
    let i = 0;
    while (i++ != 3) {
        console.log(najczestsze_elem(lista_logow) + " " + najczestsze_liczba(lista_logow));
        usun(lista_logow, najczestsze_elem(lista_logow))}})

