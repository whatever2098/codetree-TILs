import java.io.*;
import java.util.*;

public class Main {
    public static void print(int N){
        if(N < 1){ return; }

        System.out.print(N + " ");
        print(N - 1);
        System.out.print(N + " ");
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        print(N);
    }
}