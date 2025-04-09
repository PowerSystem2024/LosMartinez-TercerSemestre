// Clase abstracta DispositivoEntrada
class DispositivoEntrada {
  constructor(tipoEntrada, marca) {
    this._tipoEntrada = tipoEntrada;
    this._marca = marca;
  }

  get tipoEntrada() {
    return this._tipoEntrada;
  }

  set tipoEntrada(tipo) {
    this._tipoEntrada = tipo;
  }

  get marca() {
    return this._marca;
  }

  set marca(marca) {
    this._marca = marca;
  }
}

// Clase Raton
class Raton extends DispositivoEntrada {
  static contadorRatones = 0;

  constructor(tipoEntrada, marca) {
    super(tipoEntrada, marca);
    this._idRaton = ++Raton.contadorRatones;
  }

  toString() {
    return `Raton [ID: ${this._idRaton}, Tipo: ${this._tipoEntrada}, Marca: ${this._marca}]`;
  }
}

// Clase Teclado
class Teclado extends DispositivoEntrada {
  static contadorTeclado = 0;

  constructor(tipoEntrada, marca) {
    super(tipoEntrada, marca);
    this._idTeclado = ++Teclado.contadorTeclado;
  }

  toString() {
    return `Teclado [ID: ${this._idTeclado}, Tipo: ${this._tipoEntrada}, Marca: ${this._marca}]`;
  }
}

// Clase Monitor
class Monitor {
  static contadorMonitores = 0;

  constructor(marca, tamano) {
    this._idMonitor = ++Monitor.contadorMonitores;
    this._marca = marca;
    this._tamano = tamano;
  }

  get idMonitor() {
    return this._idMonitor;
  }

  toString() {
    return `Monitor [ID: ${this._idMonitor}, Marca: ${this._marca}, Tamaño: ${this._tamano}]`;
  }
}

// Clase Computadora
class Computadora {
  static contadorComputadoras = 0;

  constructor(nombre, monitor, teclado, raton) {
    this._idComputadora = ++Computadora.contadorComputadoras;
    this._nombre = nombre;
    this._monitor = monitor;
    this._teclado = teclado;
    this._raton = raton;
  }

  toString() {
    return `Computadora [ID: ${this._idComputadora}, Nombre: ${this._nombre}]\n` +
            `  ${this._monitor.toString()}\n` +
            `  ${this._teclado.toString()}\n` +
            `  ${this._raton.toString()}`;
  }
}

// Clase Orden
class Orden {
  static contadorOrdenes = 0;

  constructor() {
    this._idOrden = ++Orden.contadorOrdenes;
    this._computadoras = [];
  }

  agregarComputadora(computadora) {
    this._computadoras.push(computadora);
  }

  mostrarOrden() {
    let detalle = `Orden [ID: ${this._idOrden}]\n`;
    this._computadoras.forEach((compu, index) => {
      detalle += `\nComputadora ${index + 1}:\n${compu.toString()}\n`;
    });
    return detalle;
  }
}

// Ejemplos de Uso

const monitor1 = new Monitor('HP', '22 pulgadas');
const teclado1 = new Teclado('USB', 'Genius');
const raton1 = new Raton('Bluetooth', 'Logitech');
const computadora1 = new Computadora('Oficina', monitor1, teclado1, raton1);

const monitor2 = new Monitor('Dell', '27 pulgadas');
const teclado2 = new Teclado('USB-C', 'Redragon');
const raton2 = new Raton('Cable', 'Razer');
const computadora2 = new Computadora('Gamer', monitor2, teclado2, raton2);

const orden1 = new Orden();
orden1.agregarComputadora(computadora1);
orden1.agregarComputadora(computadora2);

console.log(orden1.mostrarOrden());