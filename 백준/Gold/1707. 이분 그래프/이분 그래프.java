import java.io.*;
import java.util.*;

public class Main {
	static List<List<Integer>> graph;
	static boolean[] visited;
	static int[] colors;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int K = Integer.parseInt(br.readLine());

		for (int i = 0; i < K; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());

			int node = Integer.parseInt(st.nextToken());
			int edge = Integer.parseInt(st.nextToken());

			graph = new ArrayList<>();
			colors = new int[node + 1]; // 0 -> None, 1 -> Red, -1 -> Black
			visited = new boolean[node + 1];


			for (int j = 0; j <= node; j++) {
				graph.add(new ArrayList<>());
			}

			for (int j = 0; j < edge; j++) {
				st = new StringTokenizer(br.readLine());
				int a = Integer.parseInt(st.nextToken());
				int b = Integer.parseInt(st.nextToken());
				graph.get(a).add(b);
				graph.get(b).add(a);
			}

			boolean result = true;
			for (int j = 1; j <= node; j++) {
				if (!visited[j]) {
					colors[j] = 1;
					if (!dfs(j)) {
						result = false;
					}
				}
			}

			if (result) System.out.println("YES");
			else System.out.println("NO");

		}

	}

	static boolean dfs(int curNode) {
		boolean result = true;
		visited[curNode] = true;

		for (int nextNode : graph.get(curNode)) {
			if (colors[nextNode] == colors[curNode]) {
					return false;
				}
			if (!visited[nextNode]) {
				colors[nextNode] = colors[curNode] * -1;
				result = dfs(nextNode);
			}
		}

		return result;
	}
}