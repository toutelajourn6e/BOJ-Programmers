class Solution {
    public String solution(int[] numLog) {
        String result = "";
        
        for (int i = 1; i < numLog.length; i++){
            int diff = numLog[i] - numLog[i-1];
            switch (diff) {
                case 1:
                    result += 'w';
                    break;
                case 10:
                    result += 'd';
                    break;
                case -1:
                    result += 's';
                    break;
                case -10:
                    result += 'a';
                    break;
            }
        }
        return result;
    }
}