package main;

import domain.Persona;

public class BloqueInicializacion {
    public static void main(String[] args) {
        Persona persona1 = new Persona();
        System.out.println("persona1 = " + persona1);
        Persona persona2 = new Persona();
        System.out.println("persona2 = " + persona2);
    }
}
