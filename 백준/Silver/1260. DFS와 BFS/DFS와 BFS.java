import java.io.*;
import java.util.*;

public class Main {
	static StringBuilder sb = new StringBuilder();
	static int[][] graph;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int node = Integer.parseInt(st.nextToken());
		int edge = Integer.parseInt(st.nextToken());
		int start = Integer.parseInt(st.nextToken());
		graph = new int[node+1][node+1];

		for (int i = 0; i < edge; i++) {
			StringTokenizer str = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(str.nextToken());
			int b = Integer.parseInt(str.nextToken());
			graph[a][b] = 1;
			graph[b][a] = 1;
		}

		boolean[] visited = new boolean[node + 1];

		dfs(start, visited);
		sb.append("\n");

		visited = new boolean[node + 1];

		bfs(start, visited);

		System.out.println(sb);

	}

	public static void dfs(int cur, boolean[] visited) {
		visited[cur] = true;
		sb.append(cur + " ");

		for (int i = 1; i < graph.length; i++) {
			if (graph[cur][i] == 1 && !visited[i]) {
				dfs(i, visited);
			}
		}
	}

	public static void bfs(int start, boolean[] visited) {
		Queue<Integer> q = new LinkedList<>();
		q.offer(start);
		visited[start] = true;

		while (!q.isEmpty()) {
			int cur = q.poll();
			sb.append(cur + " ");

			for (int i = 0; i < graph.length; i++) {
				if (graph[cur][i] == 1 && !visited[i]) {
					visited[i] = true;
					q.offer(i);
				}
			}
		}
	}

}