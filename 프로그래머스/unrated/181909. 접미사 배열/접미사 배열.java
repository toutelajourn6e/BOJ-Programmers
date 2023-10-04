import java.util.*;

class Solution {
    public String[] solution(String my_string) {
        ArrayList<String> suffix = new ArrayList<String>();
        for (int i = 0; i < my_string.length(); i++){
            suffix.add(my_string.substring(i, my_string.length()));
        }
        String[] answer = suffix.toArray(new String[0]);
        Arrays.sort(answer);
        return answer;
    }
}