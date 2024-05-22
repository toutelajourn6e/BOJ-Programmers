import java.util.HashMap;
import java.util.HashSet;
import java.util.List;

class Solution {
    public int[] solution(String[] gems) {
        int[] answer = new int[]{1, 1};
        int minLength = Integer.MAX_VALUE;
        int N = gems.length;
        int kind = new HashSet<String>(List.of(gems)).size();
        HashMap<String, Integer> gemCount = new HashMap<>();

        int left = 0, right = 0;
        gemCount.put(gems[left], 1);

        while (left <= right) {
            if (gemCount.size() >= kind) {
                if (gemCount.size() == kind) {
                    if ((right - left) < minLength) {
                    minLength = right - left;
                    answer[0] = left + 1;
                    answer[1] = right + 1;
                    }
                }
                gemCount.put(gems[left], gemCount.get(gems[left]) - 1);
                if (gemCount.get(gems[left]) == 0) {
                    gemCount.remove(gems[left]);
                }
                left++;
                if (left >= N) break;
            } else {
                right++;
                if (right >= N) break;
                gemCount.put(gems[right], gemCount.getOrDefault(gems[right], 0) + 1);
            }
        }

        return answer;
    }
}