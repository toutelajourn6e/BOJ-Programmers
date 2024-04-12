import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    static Deque<Integer> stack = new ArrayDeque<>();
    static int score = 0;

    public int solution(int[][] board, int[] moves) {
        for (int move : moves) {
            picking(board, move - 1);
        }
        return score;
    }

    public void picking(int[][] board, int col) {
        for (int row = 0; row < board.length; row++) {
            if (board[row][col] != 0) {
                if (!stack.isEmpty() && stack.peekLast() == board[row][col]) {
                    stack.pollLast();
                    score += 2;
                } else {
                    stack.offerLast(board[row][col]);
                }
                board[row][col] = 0;
                return;
            }
        }
    }
}