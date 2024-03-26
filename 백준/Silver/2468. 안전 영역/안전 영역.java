import java.io.*;
import java.util.*;

public class Main {
	static int N;
	static int[] dx = {-1, 1, 0, 0};
	static int[] dy = {0, 0, -1, 1};
	static int[][] map;
	static List<Integer> result = new ArrayList<>();

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());

		map = new int[N][N];

		for (int i = 0; i < N; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
			}
		}

		for (int h = 0; h <= 101; h++) {
			boolean[][] visited = new boolean[N][N];
			int count = 0;
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					if (map[i][j] > h && !visited[i][j]) {
						bfs(i, j, h, visited);
						count++;
					}
				}
			}
			result.add(count);
		}

		System.out.println(Collections.max(result));
	}

	static void bfs(int startX, int startY, int height, boolean[][] visited) {
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

				if (nx < 0 || nx >= N || ny < 0 || ny >= N) continue;
				if (map[nx][ny] <= height || visited[nx][ny]) continue;

				visited[nx][ny] = true;
				q.offer(new int[]{nx, ny});
			}
		}
	}
}