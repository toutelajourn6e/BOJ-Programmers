import java.util.Arrays;
import java.util.HashSet;

class Solution {
    static boolean[] check;
    static HashSet<String> set;

    public int solution(String[] userId, String[] bannedId) {
        check = new boolean[userId.length];
        set = new HashSet<>();

        for (int i = 0; i < bannedId.length; i++) {
            bannedId[i] = bannedId[i].replace("*", ".");
        }
        
        find(0, "", userId, bannedId);

        return set.size();
    }

    void find(int depth, String str, String[] userId, String[] bannedId) {
        if (depth == bannedId.length) {
            String tmp = "";
            String[] strArr = str.split(" ");
            Arrays.sort(strArr);
            for (String s : strArr) tmp += s;
            set.add(tmp);
            return;
        }


        for (int i = 0; i < userId.length; i++) {
            if (!check[i] && userId[i].matches(bannedId[depth])) {
                check[i] = true;
                find(depth + 1, userId[i] + " " + str, userId, bannedId);
                check[i] = false;
            }
        }
    }
}