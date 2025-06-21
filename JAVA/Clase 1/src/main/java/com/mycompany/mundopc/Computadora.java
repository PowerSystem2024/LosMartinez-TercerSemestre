package com.mycompany.mundopc;

public class Computadora {
    private int idComputadora;
    private String nombre;
    private Monitor monitor;
    private Teclado teclado;
    private Raton raton;
    private static int contadorComputadoras;

    public Computadora(String nombre, Monitor monitor, Teclado teclado, Raton raton) {
        this.idComputadora = ++contadorComputadoras;
        this.nombre = nombre;
        this.monitor = monitor;
        this.teclado = teclado;
        this.raton = raton;
    }

    @Override
    public String toString() {
        return "Computadora [ID: " + idComputadora + ", Nombre: " + nombre + "]\n" +
               "  " + monitor + "\n" +
               "  " + teclado + "\n" +
               "  " + raton;
    }
}