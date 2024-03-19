import java.io.*;
import java.util.*;

public class Main {
	static int[] dx = {-1, 1, 0, 0};
	static int[] dy = {0, 0, -1, 1};
	static char[][] map;
	static boolean[][] visited;
	static int N, M;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int[] result = new int[2];

		M = Integer.parseInt(st.nextToken());
		N = Integer.parseInt(st.nextToken());

		map = new char[N][M];
		visited = new boolean[N][M];

		for (int i = 0; i < N; i++) {
			String str = br.readLine();
			for (int j = 0; j < M; j++) {
				map[i][j] = str.charAt(j);
			}
		}

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (map[i][j] == 'W' && !visited[i][j]) {
					result[0] += bfs(i, j, 'W');
				} else if (map[i][j] == 'B' && !visited[i][j]) {
					result[1] += bfs(i, j, 'B');
				}
			}
		}

		System.out.println(result[0] + " " + result[1]);

	}

	static int bfs(int x, int y, char color) {
		Queue<int[]> q = new LinkedList<>();
		q.offer(new int[]{x, y});
		visited[x][y] = true;
		int count = 0;

		while (!q.isEmpty()) {
			int curX = q.peek()[0];
			int curY = q.peek()[1];
			q.poll();
			count++;

			for (int i = 0; i < 4; i++) {
				int nx = curX + dx[i];
				int ny = curY + dy[i];

				if (nx < 0 || nx >= N || ny < 0 || ny >= M) continue;
				if (map[nx][ny] != color || visited[nx][ny]) continue;

				visited[nx][ny] = true;
				q.offer(new int[]{nx, ny});
			}
		}
		return (int) Math.pow(count, 2);
	}
}