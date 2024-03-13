import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        HashMap<String, Integer> map = new HashMap<>();
    
        br.readLine();
    
        StringTokenizer st = new StringTokenizer(br.readLine());
        while (st.hasMoreTokens()) {
            String cardNum = st.nextToken();
            if (map.getOrDefault(cardNum, 0) == 0) {
                map.put(cardNum, 1);
            } else {
                map.put(cardNum, map.get(cardNum) + 1);
            }
        }  
    
        br.readLine();
        st = new StringTokenizer(br.readLine());
        while (st.hasMoreTokens()) {
            sb.append(map.getOrDefault(st.nextToken(), 0) + " ");
        }
    
        System.out.println(sb);
    
    }
}