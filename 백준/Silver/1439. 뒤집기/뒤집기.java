import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] count = new int[2];
        
        String s = br.readLine();
        int prev = Character.getNumericValue(s.charAt(0));
        count[prev]++;
        
        for (int i = 1; i < s.length(); i++) {
            int cur = Character.getNumericValue(s.charAt(i));
            if (prev != cur) {
                prev = cur;
                count[prev]++;
            }
        }
        
        if (count[0] == 0 || count[1] == 0) {
            System.out.println(0);
        } else {
            System.out.println(Math.min(count[0], count[1]));
        }
    }
}