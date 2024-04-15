import java.util.Arrays;

class Solution {
    public int solution(int[] stones, int k) {
        final int N = stones.length;
        int end = Arrays.stream(stones).max().getAsInt();
        int start = Arrays.stream(stones).min().getAsInt();
        int answer = Integer.MAX_VALUE;

        while (start <= end) {
            int mid = (start + end) / 2;
            int[] tmp = new int[N];
            for (int i = 0; i < N; i++) {
                tmp[i] = stones[i] - mid;
            }
            int cnt = 0;
            boolean possible = true;
            for (int num : tmp) {
                if (num <= 0) cnt++;
                else cnt = 0;
                if (cnt == k) {
                    possible = false;
                    answer = Math.min(answer, mid);
                    break;
                }
            }
            if (possible) {
                start = mid + 1;
            } else {
                end = mid - 1;
            }
        }


        return answer;
    }
}