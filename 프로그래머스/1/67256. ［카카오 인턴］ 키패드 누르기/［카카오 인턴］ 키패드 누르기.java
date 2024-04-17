import java.util.HashMap;

class Solution {
    static HashMap<Integer, int[]> row;
    public String solution(int[] numbers, String hand) {
        String answer = "";
        row = new HashMap<>();
        for (int i = 0; i <= 2; i++) {
            for (int j = (i * 3) + 1; j <= (i * 3) + 3; j++) {
                if (j % 3 == 0) row.put(j, new int[]{i+1, (j % 3) + 3});
                else row.put(j, new int[]{i+1, j % 3});
            }
        }
        row.put(0, new int[]{4, 2}); row.put(10, new int[]{4, 1});
        row.put(20, new int[]{4, 3});

        int leftThumb = 10, rightThumb = 20;

        for (int num : numbers) {
            if (num % 3 == 1) {
                answer += "L";
                leftThumb = num;
            } else if (num != 0 && (num % 3 == 0)) {
                answer += "R";
                rightThumb = num;
            } else {
                int leftDistance = Math.abs(row.get(leftThumb)[0] - row.get(num)[0]) + Math.abs(row.get(leftThumb)[1] - row.get(num)[1]);
                int rightDistance = Math.abs(row.get(rightThumb)[0] - row.get(num)[0]) + Math.abs(row.get(rightThumb)[1] - row.get(num)[1]);
                if (leftDistance < rightDistance) {
                    answer += "L";
                    leftThumb = num;
                } else if (rightDistance < leftDistance) {
                    answer += "R";
                    rightThumb = num;
                } else {
                    if (hand.equals("left")) {
                        answer += "L";
                        leftThumb = num;
                    } else {
                        answer += "R";
                        rightThumb = num;
                    }
                }
            }
        }

        return answer;
    }
}