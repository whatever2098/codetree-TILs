import java.io.*;
import java.util.*;

public class Main {
    public static void printLine(int n){
        for(int i = 0;i < n;i++){
            System.out.print("* ");
        }
        System.out.println();
    }

    public static void printStars(int n){
        if(n < 1){ return; }

        printLine(n);
        printStars(n - 1);
        printLine(n);
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        printStars(N);
    }
}