import java.io.*;
import java.util.*;

public class Main {
	static int N;
	static int[][] convenience;
	static boolean[] visited;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());

		for (int t = 0; t < T; t++) {
			N = Integer.parseInt(br.readLine());
			convenience = new int[N][2];
			visited = new boolean[N];

			StringTokenizer st = new StringTokenizer(br.readLine());
			int startX = Integer.parseInt(st.nextToken());
			int startY = Integer.parseInt(st.nextToken());

			for (int i = 0; i < N; i++) {
				st = new StringTokenizer(br.readLine());
				int x = Integer.parseInt(st.nextToken());
				int y = Integer.parseInt(st.nextToken());
				convenience[i][0] = x;
				convenience[i][1] = y;
			}

			st = new StringTokenizer(br.readLine());
			int endX = Integer.parseInt(st.nextToken());
			int endY = Integer.parseInt(st.nextToken());

			String result = bfs(startX, startY, endX, endY) ? "happy" : "sad";
			System.out.println(result);
		}
	}

	static boolean bfs(int startX, int startY, int endX, int endY) {
		Queue<int[]> pq = new PriorityQueue<>((o1, o2) -> o1[2] - o2[2]);
		pq.add(new int[]{startX, startY, 0});

		while (!pq.isEmpty()) {
			int x = pq.peek()[0];
			int y = pq.peek()[1];
			pq.poll();

			if ((Math.abs(endX - x) + Math.abs(endY - y)) <= 1000) {
				return true;
			}

			for (int i = 0; i < N; i++) {
				if (!visited[i]) {
					int nx = convenience[i][0];
					int ny = convenience[i][1];
					int distance = Math.abs(nx - x) + Math.abs(ny - y);

					if (distance > 1000) continue;

					visited[i] = true;
					pq.offer(new int[]{nx, ny, distance});
				}
			}
		}
		return false;
	}
}