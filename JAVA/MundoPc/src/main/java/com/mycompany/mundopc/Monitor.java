package com.mycompany.mundopc;

public class Monitor {
    private int idMonitor;
    private String marca;
    private String tamano;
    private static int contadorMonitores;

    public Monitor(String marca, String tamano) {
        this.idMonitor = ++contadorMonitores;
        this.marca = marca;
        this.tamano = tamano;
    }

    public int getIdMonitor() {
        return idMonitor;
    }

    @Override
    public String toString() {
        return "Monitor [ID: " + idMonitor + ", Marca: " + marca + ", Tamano: " + tamano + "]";
    }
}