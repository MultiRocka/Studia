import java.util.Scanner;

public class Kalkulator {


    public static void ostateczny() {
        Scanner scanner= new Scanner(System.in);
        int a;
        int b;
        int wybor;
        System.out.println(" 1.dodawanie \n 2.odejmowanie \n 3.mnożenie \n 4.dzielenie \n 5. pierwiastkowanie \n 6.potęgowanie \n");
        System.out.println("Wybierz co chcesz zrobić");
        wybor=scanner.nextInt();
        switch (wybor) {
            case 1:
                System.out.println("Podaj dwie liczby które chcesz dodać");
                a = scanner.nextInt();
                b = scanner.nextInt();
                dodawanie(a, b);
                Kalkulator.ostateczny();
            case 2:
                System.out.println("Podaj a: ");
                a = scanner.nextInt();
                System.out.println("Podaj b: ");
                b = scanner.nextInt();
                odejmowanie(a,b);
                Kalkulator.ostateczny();
            case 3:
                System.out.println("Podaj a: ");
                a = scanner.nextInt();
                System.out.println("Podaj b: ");
                b = scanner.nextInt();
                mnozenie(a,b);
                Kalkulator.ostateczny();
            case 4:
                System.out.println("Podaj a: ");
                a = scanner.nextInt();
                System.out.println("Podaj b: ");
                b = scanner.nextInt();
                dzielenie(a,b);
                Kalkulator.ostateczny();
            case 5:
                System.out.println("Podaj a: ");
                a = scanner.nextInt();
                pierwiastkowanie(a);
                Kalkulator.ostateczny();
            case 6:
                System.out.println("Podaj a: ");
                a = scanner.nextInt();
                System.out.println("Podaj b: ");
                b = scanner.nextInt();
                potegowanie(a,b);
                Kalkulator.ostateczny();
            case 0:
                break;
        }
    }

    public static int dodawanie(int a, int b){
        System.out.println("Wynik dodawania: "+(a+b));
        return 0;
    }
    public static int odejmowanie(int a,int b){
        System.out.println("Wynik odejmowania: "+(a-b));
        return 0;
    }
    public static int mnozenie(int a,int b){
        System.out.println("Wynik mnozenia: "+(a*b));
        return 0;
    }
    public static int dzielenie(int a,int b){
        try{
            System.out.println("Wynik dzielenia: "+(a/b));
        }
        catch(ArithmeticException e){
            System.err.println("Nie dziel przez 0");
            dzielenie(a,b);
        }
        return 0;
    }
    public static int pierwiastkowanie(double a){
        System.out.println("Wynik pierwiastkowania: "+Math.sqrt(a));
        return 0;
    }
    public static int potegowanie(int a,int b){
        System.out.println("Wynik potegowania: "+Math.pow(a,b));
        return 0;
    }

}
