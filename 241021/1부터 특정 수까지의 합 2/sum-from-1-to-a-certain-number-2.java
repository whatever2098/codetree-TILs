import java.io.*;
import java.util.*;

public class Main {
    public static int sum(int n){
        if(n == 1){ return 1; }

        return sum(n - 1) + n;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        System.out.println(sum(N));
    }
}