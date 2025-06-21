'use strict';

const promise1 = new Promise((resolve, reject) => {
    const condition = true;
    if (condition) {
        resolve('Resolved successfully');
    } else {
        reject('An error occurred');
    }
});

const delayedPromise = new Promise(resolve => {
    setTimeout(() => resolve('Saludos desde promesa, callback, función flecha y setTimeout'), 3000);
});

async function asyncGreeting() {
    return 'Saludos con promesas y async';
}

async function awaitSimplePromise() {
    const promise = new Promise(resolve => {
        resolve('Promesa con await');
    });
    console.log(await promise);
}

async function awaitPromiseWithTimeout() {
    const promise = new Promise(resolve => {
        console.log('Inicio función');
        setTimeout(() => resolve('Promesa con await y Timeout'), 3000);
        console.log('Final función');
    });
    console.log(await promise);
}

awaitPromiseWithTimeout();
