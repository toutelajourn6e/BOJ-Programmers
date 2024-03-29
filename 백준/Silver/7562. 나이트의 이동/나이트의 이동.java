import java.io.*;
import java.util.*;

public class Main {
    static int[] dx = {-1, -2, -2, -1, 1, 2, 2, 1};
    static int[] dy = {-2, -1, 1, 2, 2, 1, -1, -2};

    public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int T = Integer.parseInt(br.readLine());

		for (int t = 0; t < T; t++) {
			int N = Integer.parseInt(br.readLine());
			StringTokenizer st = new StringTokenizer(br.readLine());
			int startY = Integer.parseInt(st.nextToken());
			int startX = Integer.parseInt(st.nextToken());
			st = new StringTokenizer(br.readLine());
			int endY = Integer.parseInt(st.nextToken());
			int endX = Integer.parseInt(st.nextToken());

			bfs(N, startX, startY, endX, endY);
		}
	}

	static void bfs(int N, int startX, int startY, int endX, int endY) {
		boolean[][] visited = new boolean[N][N];
		Queue<int[]> q = new LinkedList<>();
		q.offer(new int[]{startX, startY, 0});
		visited[startX][startY] = true;

		while (!q.isEmpty()) {
			int x = q.peek()[0];
			int y = q.peek()[1];
			int d = q.peek()[2];
			q.poll();
			
			if (x == endX && y == endY) {
				System.out.println(d);
				return;
			}

			for (int i = 0; i < 8; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];

				if (nx < 0 || nx >= N || ny < 0 || ny >= N) continue;
				if (visited[nx][ny]) continue;

				visited[nx][ny] = true;
				q.offer(new int[]{nx, ny, d + 1});
			}
		}
	}
}