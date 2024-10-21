import java.io.*;
import java.util.*;

public class Main {
    public static int sumOfPow(int n){
        if(n < 10){ return n * n; }

        return sumOfPow(n / 10) + (int)Math.pow(n % 10, 2);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        System.out.println(sumOfPow(N));
    }
}