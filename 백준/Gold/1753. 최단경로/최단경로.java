import java.io.*;
import java.util.*;

class Node implements Comparable<Node>{
	int idx;
	int cost;

	Node(int idx, int cost) {
		this.idx = idx;
		this.cost = cost;
	}

	@Override
	public int compareTo(Node another) {
		return this.cost - another.cost;
	}
}

public class Main {
	static List<List<Node>> graph = new ArrayList<>();
	static int[] distance;
	static int V, E;

    public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		V = Integer.parseInt(st.nextToken());
		E = Integer.parseInt(st.nextToken());

		distance = new int[V + 1];
		Arrays.fill(distance, Integer.MAX_VALUE);

		for (int i = 0; i < V + 1; i++) {
			graph.add(new ArrayList<>());
		}

		int start = Integer.parseInt(br.readLine());

		for (int i = 0; i < E; i++) {
			String[] nodeInfo = br.readLine().split(" ");
			int u = Integer.parseInt(nodeInfo[0]);
			int v = Integer.parseInt(nodeInfo[1]);
			int w = Integer.parseInt(nodeInfo[2]);
			graph.get(u).add(new Node(v, w));
		}

		dijkstra(start);

		for (int i = 1; i < V + 1; i++) {
			if (distance[i] == Integer.MAX_VALUE) {
				System.out.println("INF");
			} else {
				System.out.println(distance[i]);
			}
		}

	}

	static void dijkstra(int start) {
		Queue<Node> pq = new PriorityQueue<>();
		pq.offer(new Node(start, 0));
		distance[start] = 0;

		while (!pq.isEmpty()) {
			Node cur = pq.poll();

			if (distance[cur.idx] < cur.cost) continue;

			for (Node next : graph.get(cur.idx)) {
				if (distance[next.idx] > distance[cur.idx] + next.cost) {
					distance[next.idx] = distance[cur.idx] + next.cost;
					pq.offer(new Node(next.idx, distance[next.idx]));
				}
			}
		}
	}
}