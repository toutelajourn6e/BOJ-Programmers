import java.io.*;
import java.util.*;
import java.util.stream.IntStream;

class Edge implements Comparable<Edge> {
	int a;
	int b;
	int cost;

	Edge(int a, int b, int cost) {
		this.a = a;
		this.b = b;
		this.cost = cost;
	}

	@Override
	public int compareTo(Edge another) {
		return Integer.compare(this.cost, another.cost);
	}
}


public class Main {
	static Queue<Edge> pq = new PriorityQueue<>();
	static int[] parent;

    public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());

		parent = IntStream.rangeClosed(0, N).toArray();

		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			int cost = Integer.parseInt(st.nextToken());
			pq.add(new Edge(a, b, cost));
		}

		int total = 0;
		while (!pq.isEmpty()) {
			Edge curEdge = pq.poll();
			int a = curEdge.a;
			int b = curEdge.b;
			int cost = curEdge.cost;

			if (find(a) != find(b)) {
				union(a, b);
				total += cost;
			}
		}

		System.out.println(total);
	}


	static int find(int x) {
		if (parent[x] == x) return x;
		else return find(parent[x]);
	}

	static void union(int a, int b) {
		int parentA = find(a);
		int parentB = find(b);

		if (parentA < parentB) parent[parentB] = parentA;
		else parent[parentA] = parentB;
	}


}