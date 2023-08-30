class Solution {
    public int solution(int a, int b) {
        String strnum = Integer.toString(a) + Integer.toString(b);
        return Integer.parseInt(strnum) >= 2 * a * b ? Integer.parseInt(strnum) : 2 * a * b;
    }
}