import java.io.*;

public class Main {
	public static char[][]square;
	public static int N;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		N = Integer.parseInt(br.readLine());

		square= new char[N][N];
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {square[i][j] = '*';
			}
		}

		star(N);

		for (char[] chars : square) {
			for (char c : chars) {
				bw.write(c);
			}
			bw.newLine();
		}

		bw.flush();
		br.close();
		bw.close();
	}

	public static void star(int size) {
		if (size == 1) {
			return;
		}

		star(size / 3);

		for (int x = 0; x < N; x += size) {
			for (int y = 0; y < N; y += size) {
				remove(x, y, size);
			}
		}
	}

	public static void remove(int x, int y, int size) {
		int middle = size / 2;
		square[x + middle][y + middle] = ' ';

		int holeSize = middle / 3;
		for (int i = 0; i <= holeSize; i++) {
			for (int j = 0; j <= holeSize; j++) {
				square[x + middle + i][y + middle + j] = ' ';
				square[x + middle + i][y + middle - j] = ' ';
				square[x + middle - i][y + middle + j] = ' ';
				square[x + middle - i][y + middle - j] = ' ';
			}
		}

	}
}