import java.util.Scanner;

public class zad3 {
    public static void naznak(){
        Scanner scan= new Scanner(System.in);
        System.out.println("Podaj liczbe");
        int liczba=scan.nextInt();
        while(!(liczba>=33 && liczba<=126)){
            liczba=scan.nextInt();
        }
        System.out.println("Twoja liczba w Ascii to "+ (char)liczba);
    }
}
