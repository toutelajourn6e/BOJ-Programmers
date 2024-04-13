import java.util.*;

class Solution {
    public int[] solution(String s) {
        HashSet<Integer> check = new HashSet<>();
        List<Integer> result = new ArrayList<>();
        String str = s.substring(2, s.length() - 2);

        String[] strArr = str.split("\\},\\{");
        Arrays.sort(strArr, ((o1, o2) -> o1.length() - o2.length()));

        for (String tuple : strArr) {
            String[] newTuple = tuple.split(",");
            for (String num : newTuple) {
                int intNum = Integer.parseInt(num);
                if (!check.contains(intNum)) {
                    result.add(intNum);
                    check.add(intNum);
                }
            }
        }

        return result.stream().mapToInt(i -> i).toArray();
    }
}