'use strict';

functionOne();
functionTwo();

function functionOne() {
    console.log('Funcion 1');
}

function functionTwo() {
    console.log('Funcion 2');
}

function print(message) {
    console.log(message);
}

function add(op1, op2, callback) {
    const result = op1 + op2;
    callback(`Resultado: ${result}`);
}

add(5, 3, print);

function asyncGreeting() {
    console.log('Saludo asincrono despues de 3 segundos');
}

setTimeout(asyncGreeting, 3000);
setTimeout(() => console.log('Saludo asincrono 2'), 4000);
setTimeout(() => console.log('Saludos asincrono 3'), 5000);

const clock = () => {
    const date = new Date();
    console.log(`${date.getHours()}:${date.getMinutes()}:${date.getSeconds()}`);
};