import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        String input = br.readLine();
        boolean laserOn = false;
        int stack = 0, count = 0;
        
        for (char c : input.toCharArray()) {
            if (c == '(') {
                laserOn = true;
                stack++;
            } else {
                if (laserOn) {
                    stack--;
                    count += stack;
                    laserOn = false;
                } else {
                    stack--;
                    count++;
                }
            }
        }
        
        System.out.println(count);
    }
}