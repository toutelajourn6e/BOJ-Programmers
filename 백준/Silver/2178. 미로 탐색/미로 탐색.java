import java.io.*;
import java.util.*;

public class Main {
	static int N, M;
	static int[][] map, distance;
	static int[] dx = {-1, 1, 0, 0};
	static int[] dy = {0, 0, -1, 1};

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		map = new int[N][M];
		distance = new int[N][M];

		for (int i = 0; i < N; i++) {
			Arrays.fill(distance[i], Integer.MAX_VALUE);
			String row = br.readLine();
			for (int j = 0; j < M; j++) {
				map[i][j] = row.charAt(j) - '0';
			}
		}

		bfs();

		System.out.println(distance[N-1][M-1]);

	}

	static void bfs() {
		Queue<int[]> q = new LinkedList<>();
		q.add(new int[] {0, 0, 1}); // x, y, distance
		distance[0][0] = 1;

		while (!q.isEmpty()) {
			int x = q.peek()[0];
			int y = q.peek()[1];
			int d = q.peek()[2];
			q.poll();

			for (int i = 0; i < 4; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];

				if (nx < 0 || nx >= N || ny < 0 || ny >= M) continue;
				if (map[nx][ny] != 1 || d + 1 >= distance[nx][ny]) continue;

				distance[nx][ny] = d + 1;
				q.offer(new int[]{nx, ny, d + 1});

			}
		}
	}
}