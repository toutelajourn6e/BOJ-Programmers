class Solution {
    public int solution(String number) {
        int ans = 0;
        for (int i = 0; i < number.length(); i++){
            char ch = number.charAt(i);
            ans += Character.getNumericValue(ch);
        }
        return ans % 9;
    }
}