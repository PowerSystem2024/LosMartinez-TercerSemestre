//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {

        // ForEach
        int edades[] = {5,6,8,9};
        for (int edad: edades) {
            System.out.println("edad = " + edad);

        }

        // AutoboxingUnboxing
        int enteroPrim = 10; //Tipo entero
        System.out.println("enteroPrim = " + enteroPrim);
        Integer entero = 10; //Tipo object con la clase Integer
        System.out.println("entero = "+ entero.doubleValue()); //autoboxing
        int entero2 = entero; //unboxing
        System.out.println("entero2 = "+ entero2);



    }
}