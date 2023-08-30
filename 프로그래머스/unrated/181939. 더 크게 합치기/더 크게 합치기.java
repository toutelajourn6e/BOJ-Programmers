class Solution {
    public int solution(int a, int b) {
        String A = Integer.toString(a);
        String B = Integer.toString(b);
        
        a = Integer.parseInt(A + B);
        b = Integer.parseInt(B + A);
        
        return a > b ? a : b;
    }
}