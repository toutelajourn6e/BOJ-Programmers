import java.io.*;
import java.util.*;

public class Main {
	static List<List<Integer>> graph = new ArrayList<>();
	static boolean[] visited;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int node = Integer.parseInt(st.nextToken());
		int edge = Integer.parseInt(st.nextToken());
		visited = new boolean[node + 1];

		for (int i = 0; i <= node; i++) {
			graph.add(new ArrayList<>());
		}

		for (int i = 0; i < edge; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			graph.get(a).add(b);
			graph.get(b).add(a);
		}

		int count = 0;
		for (int i = 1; i <= node; i++) {
			if (!visited[i]) {
				count++;
				dfs(i);
			}
		}

		System.out.println(count);
	}

	static void dfs(int curNode) {
		visited[curNode] = true;
		for (int nextNode : graph.get(curNode)) {
			if (!visited[nextNode]) {
				dfs(nextNode);
			}
		}
	}
}