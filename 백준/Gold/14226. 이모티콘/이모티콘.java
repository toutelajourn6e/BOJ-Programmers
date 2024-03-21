import java.io.*;
import java.util.*;

public class Main {
	static final int MAX = 1000;
	static int min = Integer.MAX_VALUE;
	static boolean[] visited = new boolean[MAX+1];

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int S = Integer.parseInt(st.nextToken());

		bfs(S);

		System.out.println(min);
	}

	static void bfs(int S) {
		Queue<int[]> q = new LinkedList<>();
		q.add(new int[]{1, 0, 0});

		while (!q.isEmpty()) {
			int curNum = q.peek()[0];
			int count = q.peek()[1];
			int clipBoard = q.peek()[2];
			q.poll();

			visited[curNum] = true;

			if (curNum == S) min = Math.min(min, count);


			if (curNum - 1 >= 0 && !visited[curNum - 1]) q.add(new int[]{curNum - 1, count + 1, clipBoard});
			if (count < min && curNum + clipBoard <= MAX && !visited[curNum + clipBoard]){
				q.add(new int[]{curNum + clipBoard, count + 1, clipBoard});
			}
			if (count < min) {
				q.add(new int[] {curNum, count + 1, curNum});
			}
		}
	}
}