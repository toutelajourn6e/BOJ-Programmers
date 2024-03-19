import java.io.*;
import java.util.*;

public class Main {
	static int[] dx = {-1, 1, 0, 0};
	static int[] dy = {0, 0, -1, 1};
	static int[][] map;
	static boolean[][] visited;
	static int N;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		List<Integer> result = new ArrayList<>();

		N = Integer.parseInt(br.readLine());
		map = new int[N][N];
		visited = new boolean[N][N];

		for (int i = 0; i < N; i++) {
			String str = br.readLine();
			for (int j = 0; j < N; j++) {
				map[i][j] = str.charAt(j) - '0';
			}
		}

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (map[i][j] == 1 && !visited[i][j]) {
					result.add(bfs(i, j));
				}
			}
		}

		Collections.sort(result);
		System.out.println(result.size());
		for (int k : result) {
			System.out.println(k);
		}

	}

	static int bfs(int x, int y) {
		Queue<int[]> q = new LinkedList<>();
		q.add(new int[] {x, y});
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
				if (nx < 0 || nx >= N || ny < 0 || ny >= N) continue;
				if (map[nx][ny] != 1 || visited[nx][ny]) continue;

				visited[nx][ny] = true;
				q.add(new int[]{nx, ny});
			}
		}
		return count;
	}

}