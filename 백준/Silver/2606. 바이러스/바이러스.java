import java.io.*;
import java.util.*;

public class Main {
	static List<List<Integer>> graph;
	static int count;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int node = Integer.parseInt(br.readLine());
		int edge = Integer.parseInt(br.readLine());
		graph = new ArrayList<>();

		for (int i = 0; i <= node; i++) {
			graph.add(new ArrayList<>());
		}

		for (int i = 0; i < edge; i++) {
			StringTokenizer str = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(str.nextToken());
			int b = Integer.parseInt(str.nextToken());
			graph.get(a).add(b);
			graph.get(b).add(a);
		}

		bfs(1, new boolean[node+1]);

		System.out.println(count-1);
	}

	static void bfs(int start, boolean[] visited) {
		Queue<Integer> q = new LinkedList<>();
		q.add(start);
		visited[start] = true;

		while (!q.isEmpty()) {
			int cur = q.poll();
			count++;
			for (int nextNode : graph.get(cur)) {
				if (!visited[nextNode]) {
					visited[nextNode] = true;
					q.offer(nextNode);
				}
			}
		}
	}
}