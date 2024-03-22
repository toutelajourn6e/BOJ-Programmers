import java.io.*;
import java.util.*;

public class Main {
	static int[] dx = {-1, 1, 0, 0, -1, 1, 1, -1};
	static int[] dy = {0, 0, -1, 1, -1, 1, -1, 1};
	static int[][] map, distance;
	static boolean[][] visited;
	static int N, M;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		map = new int[N][M];
		distance = new int[N][M];

		for (int i = 0; i < N; i++) {
			Arrays.fill(distance[i], Integer.MAX_VALUE);
			String[] str = br.readLine().split(" ");
			for (int j = 0; j < M; j++) {
				map[i][j] = Integer.parseInt(str[j]);
			}
		}

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (map[i][j] == 1) {
					visited = new boolean[N][M];
					bfs(i, j, 0);
				}
			}
		}


		int result = 0;
		for (int[] dist : distance) {
			for (int d : dist) {
				result = Math.max(result, d);
			}
		}

		System.out.println(result);
	}

	static void bfs(int k, int l, int dist) {
		Queue<int[]> q = new LinkedList<>();
		q.offer(new int[]{k, l, dist});
		visited[k][l] = true;

		while (!q.isEmpty()) {
			int x = q.peek()[0];
			int y = q.peek()[1];
			int d = q.peek()[2];
			q.poll();

			distance[x][y] = Math.min(distance[x][y], d);

			for (int i = 0; i < 8; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];

				if (nx < 0 || nx >= N || ny < 0 || ny >= M) continue;
				if (map[nx][ny] != 0 || visited[nx][ny]) continue;

				visited[nx][ny] = true;
				q.offer(new int[]{nx, ny, d + 1});
			}

		}
	}
}