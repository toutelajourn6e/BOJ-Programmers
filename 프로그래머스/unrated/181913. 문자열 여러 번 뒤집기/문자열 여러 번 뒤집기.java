class Solution {
    public String solution(String my_string, int[][] queries) {
        StringBuffer sb = new StringBuffer(my_string);
        
        for (int i = 0; i < queries.length; i++){
            String tmp = sb.toString();
            String before = tmp.substring(0, queries[i][0]);
            String after = tmp.substring(queries[i][1] + 1);
            String rev = tmp.substring(queries[i][0], queries[i][1] + 1);
            StringBuffer sb2 = new StringBuffer(rev).reverse();
            sb = new StringBuffer(before + sb2.toString() + after);
        }
        return sb.toString();
    }
}