import java.io.*;
import java.util.*;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int F = Integer.parseInt(st.nextToken());
		int S = Integer.parseInt(st.nextToken());
		int G = Integer.parseInt(st.nextToken());
		int U = Integer.parseInt(st.nextToken());
		int D = Integer.parseInt(st.nextToken());
		boolean[] visited = new boolean[F + 1];

		bfs(F, S, G, U, D, visited);
	}

	static void bfs(int F, int S, int G, int U, int D, boolean[] visited) {
		Queue<int[]> q = new LinkedList<>();
		q.offer(new int[]{S, 0});
		visited[S] = true;

		while (!q.isEmpty()) {
			int curFloor = q.peek()[0];
			int dist = q.peek()[1];
			q.poll();
			
			if (curFloor == G) {
				System.out.println(dist);
				return;
			}

			if (curFloor <= 0 || curFloor > F) continue;

			int upFloor = curFloor + U;
			int downFloor = curFloor - D;

			if (upFloor > 0 && upFloor <= F && !visited[upFloor]) {
				q.offer(new int[]{upFloor, dist + 1});
				visited[upFloor] = true;
			}

			if (downFloor > 0 && downFloor <= F && !visited[downFloor]) {
				q.offer(new int[]{downFloor, dist + 1});
				visited[downFloor] = true;
			}

		}

		System.out.println("use the stairs");
	}
}