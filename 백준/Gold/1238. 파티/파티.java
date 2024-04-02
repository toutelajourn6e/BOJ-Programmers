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

    public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		List<List<Node>> goToParty = new ArrayList<>();
		List<List<Node>> backToHome = new ArrayList<>();

		String[] graphInfo = br.readLine().split(" ");
		int V = Integer.parseInt(graphInfo[0]);
		int E = Integer.parseInt(graphInfo[1]);
		int X = Integer.parseInt(graphInfo[2]);

		int[] distParty = new int[V + 1];
		int[] distHome = new int[V + 1];
		Arrays.fill(distParty, Integer.MAX_VALUE);
		Arrays.fill(distHome, Integer.MAX_VALUE);

		for (int i = 0; i < V + 1; i++) {
			goToParty.add(new ArrayList<>());
			backToHome.add(new ArrayList<>());
		}

		for (int i = 0; i < E; i++) {
			String[] edgeInfo = br.readLine().split(" ");
			int a = Integer.parseInt(edgeInfo[0]);
			int b = Integer.parseInt(edgeInfo[1]);
			int c = Integer.parseInt(edgeInfo[2]);
			goToParty.get(b).add(new Node(a, c));
			backToHome.get(a).add(new Node(b, c));
		}

		dijkstra(X, distParty, goToParty);
		dijkstra(X, distHome, backToHome);

		int result = 0;
		for (int i = 1; i < V + 1; i++) {
			int sum = distParty[i] + distHome[i];
			result = Math.max(result, sum);
		}
		System.out.println(result);
	}

	static void dijkstra(int start, int[] distance, List<List<Node>> graph) {
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