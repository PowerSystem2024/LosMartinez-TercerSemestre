import java.util.Scanner;

public class CalculadoraUtn {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int option;

        do {
            showMenu();
            try {
                System.out.print("Elige una opción: ");
                option = Integer.parseInt(input.nextLine());

                if (option >= 1 && option <= 4) {
                    double operand1 = readNumber(input, "Ingresa el primer número: ");
                    double operand2 = readNumber(input, "Ingresa el segundo número: ");

                    execOperation(option, operand1, operand2);

                } else if (option != 5) {
                    System.out.println("⚠️ Opción inválida. Intenta nuevamente.");
                }

            } catch (NumberFormatException e) {
                System.out.println("❌ Entrada no válida. Por favor ingresa un número entero.");
                option = 0;
            } catch (Exception e) {
                System.out.println("❌ Error inesperado: " + e.getMessage());
                option = 0;
            }

            if (option != 5) {
                System.out.println("Continuar (Enter)");
                input.nextLine();
            }

        } while (option != 5);

        System.out.println("👋 Gracias por usar la calculadora.");
    }

    public static void showMenu() {
        System.out.println("""
            ====== Calculator Menu ======
            1. Suma
            2. Resta
            3. Multiplicación
            4. División
            5. Salir
            =============================
            """);
    }

    public static double readNumber(Scanner input, String prompt) {
        System.out.print(prompt);
        return Double.parseDouble(input.nextLine());
    }

    public static void execOperation(int option, double operand1, double operand2) {
        double result = 0.0;
        boolean valid = true;

        switch (option) {
            case 1 -> result = add(operand1, operand2);
            case 2 -> result = subtract(operand1, operand2);
            case 3 -> result = multiply(operand1, operand2);
            case 4 -> {
                if (operand2 != 0) {
                    result = divide(operand1, operand2);
                } else {
                    System.out.println("❌ Error: División por cero no permitida.");
                    valid = false;
                }
            }
        }

        if (valid) {
            System.out.println("✅ Resultado: " + result);
        }
    }

    public static double add(double a, double b) {
        return a + b;
    }

    public static double subtract(double a, double b) {
        return a - b;
    }

    public static double multiply(double a, double b) {
        return a * b;
    }

    public static double divide(double a, double b) {
        return a / b;
    }
}
