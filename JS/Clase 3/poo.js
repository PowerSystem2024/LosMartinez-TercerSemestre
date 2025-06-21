class Empleado{
    constructor(nombre, sueldo) {
        this._nombre = nombre;
        this._sueldo = sueldo;
    }

    obtenerDetalles(){
        return `Empleado: Nombre: ${this._nombre}, Sueldo: ${this._sueldo}`;
    }
}

class Gerente extends Empleado{
    constructor(nombre, sueldo, departamento){
        super(nombre, sueldo); 
        this._departamento = departamento; 
    }

    obtenerDetalles(){     
        return `Gerente: ${super.obtenerDetalles()}, Departamento: ${this._departamento}`;
    }
}

function imprimir(tipo) { 
    console.log(tipo.obtenerDetalles());
    if(tipo instanceof Gerente) { 
        console.log("Es un objeto de tipo Gerente");
        console.log(tipo._departamento); 
        
    }
    else if(tipo instanceof Empleado) { 
        console.log("Es un objeto de tipo Empleado");
    }
    else if(tipo instanceof Object) { 
        console.log("Es un objeto de tipo Object"); 
    }
    else {
        console.log("Tipo no reconocido");
    }
}

let empleado1 = new Empleado("Juan", 3000);
let gerente1 = new Gerente("Carlos", 8000, "Sistemas");

console.log(gerente1.obtenerDetalles());
console.log(empleado1.obtenerDetalles());

imprimir(empleado1);
imprimir(gerente1);