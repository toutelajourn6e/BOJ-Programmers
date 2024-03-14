import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Deque<Character> stack = new ArrayDeque<>();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        String input = br.readLine();
        boolean laserOn = false;
        int count = 0;
        
        for (char c : input.toCharArray()) {
            if (c == '(') {
                laserOn = true;
                stack.push('(');
            } else {
                if (laserOn) {
                    stack.pop();
                    count += stack.size();
                    laserOn = false;
                } else {
                    stack.pop();
                    count++;
                }
            }
        }
        
        System.out.println(count);
    }
}