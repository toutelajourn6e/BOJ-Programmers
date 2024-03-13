import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
    
        br.readLine();
        
        int[] cards = new int[20000001];
        StringTokenizer st = new StringTokenizer(br.readLine());
        while (st.hasMoreTokens()) {
            int cardNum = Integer.parseInt(st.nextToken()) + 10000000;
            cards[cardNum]++;
        }  
    
        br.readLine();
        
        st = new StringTokenizer(br.readLine());
        while (st.hasMoreTokens()) {
            int numberOfCard = cards[Integer.parseInt(st.nextToken()) + 10000000];
            sb.append(numberOfCard + " ");
        }
    
        System.out.println(sb);
    
    }
}