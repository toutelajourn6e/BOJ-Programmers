class Solution {
    public String solution(String my_string, int[][] queries) {
        for (int[] q : queries){
            int s = q[0], e = q[1];
            StringBuffer sb = new StringBuffer();
            for (int i = s; i <= e; i++){
                sb.append(my_string.charAt(i));
            }
            my_string = my_string.substring(0, s) + sb.reverse().toString() + my_string.substring(e + 1);
        }
        return my_string;
    }
}