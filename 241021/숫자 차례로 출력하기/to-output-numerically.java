import java.util.*;

public class Main {
    public static void firstPrint(int N){
        if(N < 1){ return; }

        firstPrint(N - 1);
        System.out.print(N + " ");
    }

    public static void secondPrint(int N){
        if(N < 1){ return; }

        System.out.print(N + " ");
        secondPrint(N - 1);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int N = sc.nextInt();

        firstPrint(N);
        System.out.println();
        secondPrint(N);
    }
}