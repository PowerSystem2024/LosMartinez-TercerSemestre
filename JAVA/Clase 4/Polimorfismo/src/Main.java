import domain.*;

public class Main {
    public static void main(String[] args) {
        Empleado empleado1 = new Empleado("Juan", 10000);
        determinarTipo(empleado1);
        imprimir(empleado1);

        empleado1 = new Gerente("Jose", 5000, "Sistemas");
        determinarTipo(empleado1);
        imprimir(empleado1);
    }

    public static void determinarTipo(Empleado empleado) {

        if (empleado instanceof Gerente) {
            System.out.println("\nEl empleado es de tipo Gerente");

            Gerente gerente = (Gerente) empleado;
            System.out.println("Departamento = " + gerente.getDepartamento());

        } else if (empleado instanceof Empleado) {
            System.out.println("El empleado es de tipo Empleado");

        } else if (empleado instanceof Object) {
            System.out.println("El empleado es de tipo Object");
        }
    }

    public static void imprimir(Empleado empleado) {
        System.out.println("empleado = " + empleado.obtenerDetalle());
    }
}