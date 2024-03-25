import java.io.*;
import java.util.*;

public class Main {
	static List<List<Integer>> graph;
	static boolean[] visited;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int N = Integer.parseInt(br.readLine());
		graph = new ArrayList<>();
		visited = new boolean[N + 1];

		for (int i = 0; i <= N; i++) {
			graph.add(new ArrayList<>());
		}

		StringTokenizer st = new StringTokenizer(br.readLine());
		int start = Integer.parseInt(st.nextToken());
		int end = Integer.parseInt(st.nextToken());

		int M = Integer.parseInt(br.readLine());

		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			graph.get(a).add(b);
			graph.get(b).add(a);
		}

		bfs(start, end);
	}

	static void bfs(int start, int end) {
		Queue<int[]> q = new LinkedList<>();
		q.add(new int[] {start, 0});
		visited[start] = true;

		while (!q.isEmpty()) {
			int cur = q.peek()[0];
			int dist = q.peek()[1];
			q.poll();

			for (int next : graph.get(cur)) {
				if (visited[next]) continue;
				if (next == end) {
					System.out.println(dist + 1);
					return;
				}

				visited[next] = true;
				q.offer(new int[]{next, dist + 1});
			}
		}
		System.out.println(-1);
	}
}