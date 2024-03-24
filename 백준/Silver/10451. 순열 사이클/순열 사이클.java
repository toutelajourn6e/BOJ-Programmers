import java.io.*;
import java.util.*;

public class Main {
	static int[] matrix;
	static boolean[] visited;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int T = Integer.parseInt(br.readLine());
		for (int i = 0; i < T; i++) {
			int N = Integer.parseInt(br.readLine());

			visited = new boolean[N + 1];
			matrix = new int[N + 1];

			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int k = 1; k <= N; k++) {
				matrix[k] = Integer.parseInt(st.nextToken());
			}

			int count = 0;

			for (int k = 1; k <= N; k++) {
				if (!visited[k]) {
					dfs(matrix[k], matrix[k]);
					count++;
				}
			}

			System.out.println(count);

		}
	}

	static void dfs(int startNode, int curNode) {
		visited[curNode] = true;
		if (matrix[curNode] == startNode) return;
		dfs(startNode, matrix[curNode]);
	}

}