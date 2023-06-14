public class zad2 {
    public static void suma(String ciag){
        char[] c =ciag.toCharArray();
        int suma=0;
        for(char b : c){
            if(b >=97 && b<=122 || b>=48 && b<=57)
                suma=suma+b;
        }
        System.out.println("Suma ASCII = "+suma);
    }
}
