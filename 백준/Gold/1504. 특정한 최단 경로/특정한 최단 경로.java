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
	static int V;

    public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		V = Integer.parseInt(st.nextToken());
		int E = Integer.parseInt(st.nextToken());

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

		st = new StringTokenizer(br.readLine());
		int viaFirst = Integer.parseInt(st.nextToken());
		int viaSecond = Integer.parseInt(st.nextToken());

		boolean isPossible = true;
		int startToFirstPath1 = dijkstra(1, viaFirst);
		int firstToSecondPath1 = dijkstra(viaFirst, viaSecond);
		int secondToEndPath1 = dijkstra(viaSecond, V);
		if (startToFirstPath1 == -1 || firstToSecondPath1 == -1 || secondToEndPath1 == -1) isPossible = false;

		int resultPath1 = isPossible ? startToFirstPath1 + firstToSecondPath1 + secondToEndPath1 : -1;

		int startToFirstPath2 = dijkstra(1, viaSecond);
		int firstToSecondPath2 = dijkstra(viaSecond, viaFirst);
		int secondToEndPath2 = dijkstra(viaFirst, V);
		if (startToFirstPath2 == -1 || firstToSecondPath2 == -1 || secondToEndPath2 == -1) isPossible = false;

		int resultPath2 = isPossible ? startToFirstPath2 + firstToSecondPath2 + secondToEndPath2 : -1;

		System.out.println(Math.min(resultPath1, resultPath2));
	}

	static int dijkstra(int start, int end) {
		Queue<Node> pq = new PriorityQueue<>();
		int[] distance = new int[V + 1];
		Arrays.fill(distance, Integer.MAX_VALUE);
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

		if (distance[end] == Integer.MAX_VALUE) return -1;
		else return distance[end];
	}

}