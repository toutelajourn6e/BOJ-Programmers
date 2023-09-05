class Solution {
    public int solution(int[] num_list) {
        int plus_sum = 1;
        int power_sum = 0;
        
        for (int i = 0; i < num_list.length; i++){
            plus_sum *= num_list[i];
            power_sum += num_list[i];
        }
        return plus_sum < power_sum * power_sum ? 1 : 0;
    }
}