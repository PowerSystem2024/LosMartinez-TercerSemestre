'use strict';

function revisarErroresIniciales() {
    try {
        let x = 10;
        // miFuncion();
        throw new Error('Mi Error');
    } catch (e) {
        console.log('Error: ' + e.message);
        console.log('Tipo: ' + typeof e);
    } finally {
        console.log('Termina la revisión de errores.');
    }
}

function validarResultado(resultado) {
    try {
        if (isNaN(resultado)) {
            throw new Error('El resultado no es un número');
        } else if (resultado === '') {
            throw new Error('El resultado es una cadena vacía');
        } else if (resultado > 0) {
            throw new Error('El valor es positivo');
        } else if (resultado <= 0) {
            throw new Error('El valor es negativo');
        }
    } catch (error) {
        console.log('Error: ' + error.message);
        console.log('Nombre del error: ' + error.name);
    } finally {
        console.log('Termina la revisión de errores 2.');
    }
}

revisarErroresIniciales();
console.log('Continuamos...');

let resultado = -5;
validarResultado(resultado);