import java.io.*;
import java.util.*;


public class Main {
	static int N, D;
	static int[] distance;
	static List<int[]> shortcuts = new ArrayList<>();

    public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		N = Integer.parseInt(st.nextToken());
		D = Integer.parseInt(st.nextToken());
		distance = new int[D + 1];
		Arrays.fill(distance, Integer.MAX_VALUE);

		for (int i = 0; i < N; i++) {
			String[] highwayInfo = br.readLine().split(" ");
			int a = Integer.parseInt(highwayInfo[0]);
			int b = Integer.parseInt(highwayInfo[1]);
			int cost = Integer.parseInt(highwayInfo[2]);
			shortcuts.add(new int[]{a, b, cost});
		}

		dijkstra();
		System.out.println(distance[D]);
	}

	static void dijkstra() {
		Queue<int[]> pq = new PriorityQueue<>((o1, o2) -> o1[1] - o2[1]);
		distance[0] = 0;
		pq.offer(new int[]{0, 0});

		while (!pq.isEmpty()) {
			int idx = pq.peek()[0];
			int cost = pq.peek()[1];
			pq.poll();

			if (idx > D || distance[idx] < cost) continue;
			distance[idx] = Math.min(distance[idx], cost);

			for (int[] shortcut : shortcuts) {
				int a = shortcut[0];
				int b = shortcut[1];
				int c = shortcut[2];

				if (a == idx && b <= D) {
					if (distance[b] > distance[a] + c) {
						distance[b] = distance[a] + c;
						pq.offer(new int[]{b, distance[b]});
					}
				}
			}
			pq.offer(new int[]{idx + 1, cost + 1});
		}
	}
}