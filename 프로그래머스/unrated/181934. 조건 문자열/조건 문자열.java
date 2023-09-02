class Solution {
    public int solution(String ineq, String eq, int n, int m) {
        int ans;
        
        if (eq.equals("!")){
            if (ineq.equals("<"))
                ans = n < m ? 1 : 0;
            else
                ans = n > m ? 1 : 0;
        }
        else {
            if (ineq.equals("<"))
                ans = n <= m ? 1 : 0;
            else
                ans = n >= m ? 1 : 0;
        }
        return ans;
    }
}