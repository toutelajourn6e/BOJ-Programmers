import java.io.*;
import java.util.*;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		while (true) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int K = Integer.parseInt(st.nextToken());

			if (K == 0) break;

			int[] arr = new int[K];
			for (int i = 0; i < K; i++) {
				arr[i] = Integer.parseInt(st.nextToken());
			}

			combination(arr, new boolean[K], 6, 0, 0);
			System.out.println();
		}
	}

	static void combination(int[] arr, boolean[] visited, int r, int depth, int start) {
		if (depth == r) {
			for (int i = 0; i < visited.length; i++) {
				if (visited[i]) {
					System.out.print(arr[i] + " ");
				}
			}
			System.out.println();
			return;
		}

		for (int i = start; i < arr.length; i++) {
			if (!visited[i]) {
				visited[i] = true;
				combination(arr, visited, r, depth + 1, i + 1);
				visited[i] = false;
			}
		}
	}
}