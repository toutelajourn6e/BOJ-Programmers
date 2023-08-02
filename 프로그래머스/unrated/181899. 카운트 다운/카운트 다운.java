class Solution {
    public int[] solution(int start, int end) {
        int size = (start - end) + 1;
        int[] ans = new int[size];
        int cnt = start;
        for (int i = 0; i < ans.length; i++) {
            ans[i] = cnt;
            cnt--;
        }
        return ans;
    }
}