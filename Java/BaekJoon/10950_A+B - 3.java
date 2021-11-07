import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < t; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int tc1 = Integer.parseInt(st.nextToken());
            int tc2 = Integer.parseInt(st.nextToken());
            sb.append(tc1+tc2).append("\n");
        }

        br.close();

        System.out.println(sb);
    }
}