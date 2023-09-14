class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int[] ans = new int[queries.length];
        
        for (int i = 0; i < queries.length; i++){
            int tmp = 10000000;
            for (int k = queries[i][0]; k <= queries[i][1]; k++){
                if (arr[k] > queries[i][2])
                    tmp = Math.min(tmp, arr[k]);
            }
        ans[i] = tmp >= 10000000 ? -1 : tmp;
        }
        return ans;
    }
}