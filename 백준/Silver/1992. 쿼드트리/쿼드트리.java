import java.io.*;

public class Main {
	public static int[][] img;
	public static StringBuilder sb = new StringBuilder();

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		img = new int[N][N];

		for (int i = 0; i < N; i++) {
			String row = br.readLine();

			for (int j = 0; j < N; j++) {
				img[i][j] = row.charAt(j) - '0';
			}
		}

		divide(N, 0, 0);
		System.out.println(sb);

	}

	public static void divide(int size, int x, int y) {
		if (isPossible(size, x, y)) {
			sb.append(img[x][y]);
			return;
		}

		int newSize = size / 2;

		sb.append("(");

		divide(newSize, x, y);
		divide(newSize, x, y + newSize);
		divide(newSize, x + newSize, y);
		divide(newSize, x + newSize, y + newSize);

		sb.append(")");
	}

	public static boolean isPossible(int size, int x, int y) {
		int value = img[x][y];

		for (int i = x; i < x + size; i++) {
			for (int j = y; j < y + size; j++) {
				if (img[i][j] != value) {
					return false;
				}
			}
		}
		return true;
	}
}