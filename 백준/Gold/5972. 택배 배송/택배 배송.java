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
		StringTokenizer st = new StringTokenizer(br.readLine());

		int V = Integer.parseInt(st.nextToken());
		int E = Integer.parseInt(st.nextToken());
		distance = new int[V + 1];
		Arrays.fill(distance, Integer.MAX_VALUE);

		for (int i = 0; i < V + 1; i++) {
			graph.add(new ArrayList<>());
		}

		for (int i = 0; i < E; i++) {
			String[] edgeInfo = br.readLine().split(" ");
			int a = Integer.parseInt(edgeInfo[0]);
			int b = Integer.parseInt(edgeInfo[1]);
			int c = Integer.parseInt(edgeInfo[2]);
			graph.get(a).add(new Node(b, c));
			graph.get(b).add(new Node(a, c));
		}

		dijkstra(1);
		System.out.println(distance[V]);
		
	}

	static void dijkstra(int start) {
		Queue<Node> pq = new PriorityQueue<>();
		distance[start] = 0;
		pq.offer(new Node(start, 0));

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