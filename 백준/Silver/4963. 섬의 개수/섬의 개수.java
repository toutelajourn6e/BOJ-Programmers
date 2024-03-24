import java.io.*;
import java.util.*;

public class Main {
	static int[] dx = {-1, 1, 0, 0, -1, 1, -1, 1};
	static int[] dy = {0, 0, -1, 1, -1, 1, 1, -1};
	static int N, M;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		while (true) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			M = Integer.parseInt(st.nextToken());
			N = Integer.parseInt(st.nextToken());
			if (N == 0 && M == 0) break;

			int[][] map = new int[N][M];
			boolean[][] visited = new boolean[N][M];

			for (int i = 0; i < N; i++) {
				String[] str = br.readLine().split(" ");
				for (int j = 0; j < M; j++) {
					map[i][j] = Integer.parseInt(str[j]);
				}
			}

			int count = 0;

			for (int i = 0; i < N; i++) {
				for (int j = 0; j < M; j++) {
					if (map[i][j] == 1 && !visited[i][j]) {
						bfs(i, j, map, visited);
						count++;
					}
				}
			}

			System.out.println(count);
		}
	}

	static void bfs(int startX, int startY, int[][] map, boolean[][] visited) {
		Queue<int[]> q = new LinkedList<>();
		q.offer(new int[]{startX, startY});
		visited[startX][startY] = true;

		while (!q.isEmpty()) {
			int x = q.peek()[0];
			int y = q.peek()[1];
			q.poll();
			
			for (int i = 0; i < 8; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];

				if (nx < 0 || nx >= N || ny < 0 || ny >= M) continue;
				if (map[nx][ny] == 0 || visited[nx][ny]) continue;

				visited[nx][ny] = true;
				q.offer(new int[]{nx, ny});

			}
		}
	}

}