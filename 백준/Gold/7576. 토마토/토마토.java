import java.io.*;
import java.util.*;

public class Main {
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    static int[][] tomatos;
    static int N, M;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
		tomatos = new int[N][M];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                tomatos[i][j] = Integer.parseInt(st.nextToken());
            }
        }

		Queue<int[]> q = new LinkedList<>();
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (tomatos[i][j] == 1) {
					q.offer(new int[]{i, j, 0});
				}
			}
		}

		int result = bfs(q);

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (tomatos[i][j] == 0) {
					System.out.println(-1);
					return;
				}
			}
		}
		System.out.println(result);
    }


	static int bfs (Queue<int[]> q){
		int day = 0;

		while (!q.isEmpty()) {
			int x = q.peek()[0];
			int y = q.peek()[1];
			int d = q.peek()[2];
			q.poll();

			day = Math.max(day, d);

			for (int i = 0; i < 4; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];

				if (nx < 0 || nx >= N || ny < 0 || ny >= M) continue;
				if (tomatos[nx][ny] != 0) continue;

				tomatos[nx][ny] = 1;
				q.offer(new int[]{nx, ny, d + 1});
			}
		}

		return day;
	}
}