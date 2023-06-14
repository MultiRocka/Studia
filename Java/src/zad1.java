public class zad1 {
    public static void ob(char znak,String ciag){
    char[] c =ciag.toCharArray();
    int licz = 0;
    for(char b : c){
        if(b == znak)
        licz++;
    }
        System.out.println("Znak powtarza sie tyle razy = "+licz);
    }
}
