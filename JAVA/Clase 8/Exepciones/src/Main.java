import static domain.Aritmetica.division;
import domain.OperacionExcepcion;

public class Main {
    public static void main(String[] args) {
        int resultado = 0;

        try {
            resultado = division(2, 0);
        } catch (OperacionExcepcion e) {
            System.out.println("Ocurrió un error de tipo OperacionExcepcion");
            System.out.println(e.getMessage());
        } catch (Exception e) {
            System.out.println("Ocurrió un Error");
            e.printStackTrace(System.out);
            System.out.println(e.getMessage());
        } finally {
            System.out.println("Se reviso la division entre cero");
        }
        System.out.println("La variable de resultado tiene como valor: " + resultado);
    }
}