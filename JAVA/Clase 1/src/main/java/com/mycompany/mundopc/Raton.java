package com.mycompany.mundopc;

public class Raton extends DispositivoEntrada {
    private int idRaton;
    private static int contadorRatones;

    public Raton(String tipoEntrada, String marca) {
        super(tipoEntrada, marca);
        this.idRaton = ++contadorRatones;
    }

    @Override
    public String toString() {
        return "Raton [ID: " + idRaton + ", Tipo Entrada: " + getTipoEntrada() + ", Marca: " + getMarca() + "]";
    }
}