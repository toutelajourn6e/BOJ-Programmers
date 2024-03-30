import java.io.*;
import java.util.*;

public class Main {
	static int N, M, K;
	static int[][] map;
	static int[][] visited;
	static int[] dx = {-1, 1, 0, 0};
	static int[] dy = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());
		map = new int[N][M];
		visited = new int[N][M];

		for (int i = 0; i < N; i++) {
			char[] chars = br.readLine().toCharArray();
			for (int j = 0; j < M; j++) {
				map[i][j] = chars[j] == '.' ? 0 : 1;
			}
		}

		st = new StringTokenizer(br.readLine());
		int startX = Integer.parseInt(st.nextToken()) - 1;
		int startY = Integer.parseInt(st.nextToken()) - 1;
		int endX = Integer.parseInt(st.nextToken()) - 1;
		int endY = Integer.parseInt(st.nextToken()) - 1;

		bfs(startX, startY, endX, endY);
		int result = visited[endX][endY] != 0 ? visited[endX][endY] : -1;
		System.out.println(result);
	}

	static void bfs(int startX, int startY, int endX, int endY) {
		Queue<int[]> q = new LinkedList<>();
		q.offer(new int[]{startX, startY});

		while (!q.isEmpty()) {
			int x = q.peek()[0];
			int y = q.peek()[1];
			q.poll();

			if (x == endX && y == endY) {
				return;
			}

			for (int i = 0; i < 4; i++) {
				for (int k = 1; k <= K; k++) {
					int nx = x + (dx[i] * k);
					int ny = y + (dy[i] * k);

					if (nx >= 0 && nx < N && ny >= 0 && ny < M && map[nx][ny] == 0) {
						if (visited[nx][ny] == 0) {
							visited[nx][ny] = visited[x][y] + 1;
							q.offer(new int[]{nx, ny});
						} else if (visited[nx][ny] <= visited[x][y]) {
							break;
						}
					} else {
						break;
					}
				}
			}
		}
	}
}