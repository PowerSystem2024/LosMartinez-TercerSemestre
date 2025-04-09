package com.mycompany.mundopc;

import java.util.ArrayList;

public class Orden {
    private int idOrden;
    private ArrayList<Computadora> computadoras;
    private static int contadorOrdenes;
    private static final int MAX_COMPUTADORAS = 10;

    public Orden() {
        this.idOrden = ++contadorOrdenes;
        this.computadoras = new ArrayList<>();
    }

    public void agregarComputadora(Computadora computadora) {
        if (computadoras.size() < MAX_COMPUTADORAS) {
            computadoras.add(computadora);
        } else {
            System.out.println("No se pueden agregar más computadoras a la orden.");
        }
    }

    public void mostrarOrden() {
        System.out.println("Orden #" + idOrden);
        for (Computadora comp : computadoras) {
            System.out.println(comp);
        }
    }
}