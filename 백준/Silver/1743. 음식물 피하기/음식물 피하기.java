import java.io.*;
import java.util.*;

public class Main {
	static int[][] map;
	static boolean[][] visited;
	static int N, M;
	static int[] dx = {-1, 1, 0, 0};
	static int[] dy = {0, 0, -1, 1};

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());

		map = new int[N][M];
		visited = new boolean[N][M];

		for (int i = 0; i < K; i++) {
			st = new StringTokenizer(br.readLine());
			int x = Integer.parseInt(st.nextToken()) - 1;
			int y = Integer.parseInt(st.nextToken()) - 1;
			map[x][y] = 1;
		}

		int result = 0;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (!visited[i][j] && map[i][j] == 1) {
					result = Math.max(bfs(i, j), result);
				}
			}
		}

		System.out.println(result);

	}

	static int bfs(int i, int j) {
		int count = 0;
		Queue<int[]> q = new LinkedList<>();
		q.add(new int[]{i, j});
		visited[i][j] = true;

		while (!q.isEmpty()) {
			int x = q.peek()[0];
			int y = q.peek()[1];
			q.poll();
			count++;

			for (int k= 0; k < 4; k++) {
				int nx = x + dx[k];
				int ny = y + dy[k];

				if (nx < 0 || nx >= N || ny < 0 || ny >= M) continue;
				if (map[nx][ny] != 1 || visited[nx][ny]) continue;

				visited[nx][ny] = true;
				q.offer(new int[]{nx, ny});
			}
		}
		return count;
	}
}