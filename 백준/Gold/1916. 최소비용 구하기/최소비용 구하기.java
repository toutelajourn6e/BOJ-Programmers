import java.io.*;
import java.util.*;

class Node implements Comparable<Node> {
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

    public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int V = Integer.parseInt(br.readLine());
		int E = Integer.parseInt(br.readLine());
		distance = new int[V + 1];
		Arrays.fill(distance, Integer.MAX_VALUE);

		for (int i = 0; i < V + 1; i++) {
			graph.add(new ArrayList<>());
		}

		for (int i = 0; i < E; i++) {
			String[] nodeInfo = br.readLine().split(" ");
			int a = Integer.parseInt(nodeInfo[0]);
			int b = Integer.parseInt(nodeInfo[1]);
			int c = Integer.parseInt(nodeInfo[2]);
			graph.get(a).add(new Node(b, c));
		}

		String[] info = br.readLine().split(" ");
		int departure = Integer.parseInt(info[0]);
		int arrival = Integer.parseInt(info[1]);

		dijkstra(departure);
		System.out.println(distance[arrival]);
	}

	static void dijkstra(int departure) {
		Queue<Node> pq = new PriorityQueue<>();
		distance[departure] = 0;
		pq.offer(new Node(departure, 0));

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