package com.mycompany.mundopc;

public class MundoPc {
    public static void main(String[] args) {
        Orden orden = new Orden();
        
        Monitor monitor1 = new Monitor("HP", "22 pulgadas");
        Teclado teclado1 = new Teclado("USB", "Genius");
        Raton raton1 = new Raton("Bluetooth", "Logitech");
        Computadora computadora1 = new Computadora("Oficina", monitor1, teclado1, raton1);

        Monitor monitor2 = new Monitor("Dell", "27 pulgadas");
        Teclado teclado2 = new Teclado("USB-C", "Redragon");
        Raton raton2 = new Raton("Cable", "Razer");
        Computadora computadora2 = new Computadora("Gamer", monitor2, teclado2, raton2);

        Monitor monitor3 = new Monitor("LG", "24 pulgadas");
        Teclado teclado3 = new Teclado("Bluetooth", "Logitech");
        Raton raton3 = new Raton("Inalambrico", "HP");
        Computadora computadora3 = new Computadora("Diseno", monitor3, teclado3, raton3);

        Monitor monitor4 = new Monitor("Samsung", "32 pulgadas");
        Teclado teclado4 = new Teclado("USB", "Microsoft");
        Raton raton4 = new Raton("USB", "Genius");
        Computadora computadora4 = new Computadora("Multimedia", monitor4, teclado4, raton4);

        Monitor monitor5 = new Monitor("ViewSonic", "21 pulgadas");
        Teclado teclado5 = new Teclado("USB", "Dell");
        Raton raton5 = new Raton("Bluetooth", "Dell");
        Computadora computadora5 = new Computadora("Oficina 2", monitor5, teclado5, raton5);

        Monitor monitor6 = new Monitor("AOC", "23.8 pulgadas");
        Teclado teclado6 = new Teclado("Bluetooth", "Logitech");
        Raton raton6 = new Raton("Bluetooth", "Logitech");
        Computadora computadora6 = new Computadora("Streaming", monitor6, teclado6, raton6);

        Monitor monitor7 = new Monitor("HP", "19 pulgadas");
        Teclado teclado7 = new Teclado("USB", "Genius");
        Raton raton7 = new Raton("USB", "Genius");
        Computadora computadora7 = new Computadora("Servidor", monitor7, teclado7, raton7);

        Monitor monitor8 = new Monitor("Asus", "25 pulgadas");
        Teclado teclado8 = new Teclado("Mecanico", "Redragon");
        Raton raton8 = new Raton("Inalambrico", "Razer");
        Computadora computadora8 = new Computadora("Desarrollo", monitor8, teclado8, raton8);

        Monitor monitor9 = new Monitor("BenQ", "24 pulgadas");
        Teclado teclado9 = new Teclado("USB-C", "HP");
        Raton raton9 = new Raton("Cable", "Microsoft");
        Computadora computadora9 = new Computadora("Escritorio", monitor9, teclado9, raton9);

        Monitor monitor10 = new Monitor("Lenovo", "14 pulgadas");
        Teclado teclado10 = new Teclado("Integrado", "Lenovo");
        Raton raton10 = new Raton("Touchpad", "Lenovo");
        Computadora computadora10 = new Computadora("Portatil", monitor10, teclado10, raton10);

        orden.agregarComputadora(computadora1);
        orden.agregarComputadora(computadora2);
        orden.agregarComputadora(computadora3);
        orden.agregarComputadora(computadora4);
        orden.agregarComputadora(computadora5);
        orden.agregarComputadora(computadora6);
        orden.agregarComputadora(computadora7);
        orden.agregarComputadora(computadora8);
        orden.agregarComputadora(computadora9);
        orden.agregarComputadora(computadora10);

        orden.mostrarOrden();
    }
}