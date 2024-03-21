import java.io.*;
import java.util.*;

public class Main {
	static Queue<Integer> pq = new PriorityQueue<>();
	static final int MAX = 100000;
	static int min = Integer.MAX_VALUE;
	static boolean[] visited = new boolean[MAX+1];

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());

		bfs(N, K);

		System.out.println(min);
	}

	static void bfs(int N, int K) {
		Queue<int[]> q = new LinkedList<>();
		q.add(new int[]{N, 0});

		while (!q.isEmpty()) {
			int curNum = q.peek()[0];
			int count = q.peek()[1];
			q.poll();

			visited[curNum] = true;

			if (curNum == K) min = Math.min(min, count);

			if (curNum * 2 <= MAX && !visited[curNum * 2]) q.add(new int[]{curNum * 2, count});
			if (curNum + 1 <= MAX && !visited[curNum + 1]) q.add(new int[]{curNum + 1, count + 1});
			if (curNum - 1 >= 0 && !visited[curNum - 1]) q.add(new int[]{curNum - 1, count + 1});
		}
	}
}