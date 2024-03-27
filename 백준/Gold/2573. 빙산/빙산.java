import java.io.*;
import java.util.*;

public class Main {
	static int[][] map;
	static int N, M;
	static int[] dx = {-1, 1, 0, 0};
	static int[] dy = {0, 0, -1, 1};

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		map = new int[N][M];

		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < M; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
			}
		}

		for (int k = 1; k <= Integer.MAX_VALUE; k++) {
			boolean[][] meltVisited = new boolean[N][M];
			boolean[][] visited = new boolean[N][M];

			for (int i = 0; i < N; i++) {
				for (int j = 0; j < M; j++) {
					if (map[i][j] != 0 && !meltVisited[i][j]) {
						melt(i, j, meltVisited);
					}
				}
			}

			int count = 0;
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < M; j++) {
					if (map[i][j] != 0 && !visited[i][j]) {
						bfs(i, j, visited);
						count++;
					}
				}
			}
			if (count == 0) {
				System.out.println(0);
				break;
			}
			if (count > 1) {
				System.out.println(k);
				break;
			}
		}

	}

	static void melt(int startX, int startY, boolean[][] visited) {
		Queue<int[]> q = new LinkedList<>();
		q.offer(new int[]{startX, startY});
		visited[startX][startY] = true;

		while (!q.isEmpty()) {
			int x = q.peek()[0];
			int y = q.peek()[1];
			q.poll();

			for (int i = 0; i < 4; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];

				if (map[nx][ny] == 0 && !visited[nx][ny]) {
					if (map[x][y] > 0) {
						map[x][y]--;
					} else {
						break;
					}
				}
			}

			for (int i = 0; i < 4; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];

				if (map[nx][ny] == 0 || visited[nx][ny]) continue;

				visited[nx][ny] = true;
				q.offer(new int[]{nx, ny});
			}
		}
	}

	static void bfs(int startX, int startY, boolean[][] visited) {
		Queue<int[]> q = new LinkedList<>();
		q.offer(new int[]{startX, startY});
		visited[startX][startY] = true;

		while (!q.isEmpty()) {
			int x = q.peek()[0];
			int y = q.peek()[1];
			q.poll();

			for (int i = 0; i < 4; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];

				if (map[nx][ny] == 0 || visited[nx][ny]) continue;

				visited[nx][ny] = true;
				q.offer(new int[]{nx, ny});
			}
		}
	}
}