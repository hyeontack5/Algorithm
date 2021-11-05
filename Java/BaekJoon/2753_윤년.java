import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int year = Integer.parseInt(br.readLine());
        int flag = 0;

        if (((year % 4 == 0) && (year % 100 != 0)) || (year % 400 == 0)) {
            flag = 1;
        }
        System.out.println(flag);
    }
}