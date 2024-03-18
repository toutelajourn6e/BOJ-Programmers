import java.io.*;

public class Main {
	public static int[][] graph;
	public static int N;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();

		N = Integer.parseInt(br.readLine());
		graph = new int[N][N];

		for (int i = 0; i < N; i++) {
			String[] row = br.readLine().split(" ");
			for (int j = 0; j < N; j++) {
				graph[i][j] = Integer.parseInt(row[j]);
			}
		}

		for (int k = 0; k < N; k++) {
			for (int a = 0; a < N; a++) {
				for (int b = 0; b < N; b++) {
					if (graph[a][k] == 1 && graph[k][b] == 1) {
						graph[a][b] = 1;
					}
				}
			}
		}

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				sb.append(graph[i][j] + " ");
			}
			sb.append("\n");
		}

		System.out.println(sb);

	}

}