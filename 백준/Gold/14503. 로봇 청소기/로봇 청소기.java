import java.io.*;

public class Main {
	public static int[][] room;
	public static int clear;
	public static int[] dx = {-1, 0, 1, 0};
	public static int[] dy = {0, 1, 0, -1};

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		String[] size = br.readLine().split(" ");
		int N = Integer.parseInt(size[0]);
		int M = Integer.parseInt(size[1]);
		room = new int[N][M];

		String[] point = br.readLine().split(" ");
		int x = Integer.parseInt(point[0]);
		int y = Integer.parseInt(point[1]);
		int d = Integer.parseInt(point[2]);

		for (int i = 0; i < N; i++) {
			String[] s = br.readLine().split(" ");
			for (int j = 0; j < M; j++) {
				room[i][j] = Integer.parseInt(s[j]);
			}
		}


		operate(x, y, d);

		System.out.println(clear);
	}

	public static void operate(int x, int y, int d) {
		if (room[x][y] == 0) {
			clear++;
			room[x][y] = -1;
		}

		for (int i = 0; i < 4; i++) {
			d = (d + 3) % 4;
			int nx = x + dx[d];
			int ny = y + dy[d];

			if (nx >= 0 && ny >= 0 && room[nx][ny] == 0) {
				operate(nx, ny, d);
				return;
			}
		}

		int back = (d + 2) % 4;
		int backX = x + dx[back];
		int backY = y + dy[back];

		if (backX >= 0 && backY >= 0 && room[backX][backY] != 1) {
			operate(backX, backY, d);
		}

	}
}