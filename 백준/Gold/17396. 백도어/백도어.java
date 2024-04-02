import java.io.*;
import java.util.*;

class Node implements Comparable<Node> {
	long idx;
	long cost;

	Node(long idx, long cost) {
		this.idx = idx;
		this.cost = cost;
	}

	@Override
	public int compareTo(Node another) {
		return Long.compare(this.cost, another.cost);
	}
}


public class Main {
	static List<List<Node>> graph = new ArrayList<>();
	static long[] distance;

    public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int V = Integer.parseInt(st.nextToken());
		int E = Integer.parseInt(st.nextToken());
		distance = new long[V];
		Arrays.fill(distance, Long.MAX_VALUE);

		for (int i = 0; i < V; i++) {
			graph.add(new ArrayList<>());
		}

		int[] isImpossible = new int[V];
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < V - 1; i++) {
			isImpossible[i] = Integer.parseInt(st.nextToken());
		}

		for (int i = 0; i < E; i++) {
			String[] edgeInfo = br.readLine().split(" ");
			int a = Integer.parseInt(edgeInfo[0]);
			int b = Integer.parseInt(edgeInfo[1]);
			int c = Integer.parseInt(edgeInfo[2]);
			if (isImpossible[a] == 0 && isImpossible[b] == 0) {
				graph.get(a).add(new Node(b, c));
				graph.get(b).add(new Node(a, c));
			}
		}

		dijkstra(0);
		long result = distance[V - 1] == Long.MAX_VALUE ? -1 : distance[V - 1];
		System.out.println(result);
	}

	static void dijkstra(int start) {
		Queue<Node> pq = new PriorityQueue<>();
		distance[start] = 0;
		pq.offer(new Node(start, 0));

		while (!pq.isEmpty()) {
			Node cur = pq.poll();
			int curIdx = (int) cur.idx;

			if (distance[curIdx] < cur.cost) continue;

			for (Node next : graph.get(curIdx)) {
				int nextIdx = (int) next.idx;
				if (distance[nextIdx] > distance[curIdx] + next.cost) {
					distance[nextIdx] = distance[curIdx] + next.cost;
					pq.offer(new Node(next.idx, distance[nextIdx]));
				}
			}
		}
	}
}