import java.util.ArrayList;

class Solution {
    public int[] solution(String[] intStrs, int k, int s, int l) {
        ArrayList<Integer> result = new ArrayList<Integer>();
        
        for (String str : intStrs){
            String tmp = "";
            for (int i = s; i < s + l; i++){
                tmp += str.charAt(i);
            }
            if (Integer.parseInt(tmp) > k)
                result.add(Integer.parseInt(tmp));
        }
        return result.stream().mapToInt(i->i).toArray();
    }
}