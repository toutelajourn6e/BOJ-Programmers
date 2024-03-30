import java.io.*;
import java.util.*;

public class Main {
	static int N, K;
	static int[] graph = new int[100001];

    public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		N = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());

		int ans = bfs(N);

		System.out.println(graph[K]);
		System.out.println(ans);
	}

	static int bfs(int N) {
		int result = 0;
		Queue<Integer> q = new LinkedList<>();
		q.offer(N);

		while (!q.isEmpty()) {
			int cur = q.poll();

			if (cur == K) {
				result++;
				continue;
			}

			for (int i : new int[]{cur + 1, cur - 1, cur * 2}) {
				if (i >= 0 && i <= 100000 && (graph[i] == 0 || graph[i] >= graph[cur] + 1)) {
					graph[i] = graph[cur] + 1;
					q.offer(i);
				}
			}
		}
		return result;
	}
}