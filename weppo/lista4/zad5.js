const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
})

readline.question(`Jakie jest Twoje imię? `, (imie) => {
    console.log(`Witaj ${imie}!`)
    readline.close()
})