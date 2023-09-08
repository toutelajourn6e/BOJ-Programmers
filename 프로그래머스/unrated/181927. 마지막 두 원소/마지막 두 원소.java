class Solution {
    public int[] solution(int[] num_list) {
        int[] ans = new int[num_list.length + 1];
        for (int i = 0; i < num_list.length; i++)
            ans[i] = num_list[i];
        
        int last = num_list[num_list.length-1];
        int before_last = num_list[num_list.length-2];
        
        ans[ans.length-1] = last > before_last ? last - before_last : last * 2;
        return ans;
    }
}