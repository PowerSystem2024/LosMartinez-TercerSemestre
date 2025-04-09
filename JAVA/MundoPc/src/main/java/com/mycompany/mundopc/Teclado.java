package com.mycompany.mundopc;

public class Teclado extends DispositivoEntrada {
    private int idTeclado;
    private static int contadorTeclado;

    public Teclado(String tipoEntrada, String marca) {
        super(tipoEntrada, marca);
        this.idTeclado = ++contadorTeclado;
    }

    @Override
    public String toString() {
        return "Teclado [ID: " + idTeclado + ", Tipo Entrada: " + getTipoEntrada() + ", Marca: " + getMarca() + "]";
    }
}