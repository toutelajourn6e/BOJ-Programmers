import java.util.ArrayList;

class Solution {
    public int[] solution(int n) {
        ArrayList<Integer> ans = new ArrayList<Integer>();
        ans.add(n);
        
        while (n != 1){
            if (n % 2 == 0) n /= 2;    
            else n = (3 * n) + 1;
            ans.add(n);
        }
        return ans.stream().mapToInt(i->i).toArray();
    }
}