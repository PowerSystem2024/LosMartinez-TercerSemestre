import domain.*;

public class Main {
    public static void main(String[] args) {
        Empleado empleado = new Escritor("Ana", 5000, TipoEscritura.CLASICO);
        System.out.println(empleado.obtenerDetalles());

        Escritor escritor = (Escritor)empleado;
        escritor.getTipoEscritura();

        Empleado empleado2 = escritor;
        System.out.println(empleado2.obtenerDetalles());
    }
}