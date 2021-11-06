import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());

        br.close();

        for (int i = n; i >= 1; i--) {
            sb.append(i).append("\n");
        }
        System.out.println(sb);
    }
}