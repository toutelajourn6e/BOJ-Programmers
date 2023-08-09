class Solution {
    public int solution(int n) {
        int ans = 0;
        
        for (int i = n; i > 0; i--){
            if (n % i == 0)
                ans += i;
        }
        return ans;
    }
}