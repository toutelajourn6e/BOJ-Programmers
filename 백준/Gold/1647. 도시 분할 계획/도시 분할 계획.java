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
			String[] str = br.readLine().split(" ");
			int a = Integer.parseInt(str[0]);
			int b = Integer.parseInt(str[1]);
			int cost = Integer.parseInt(str[2]);
			pq.add(new Edge(a, b, cost));
		}

		int edgeCount = 0;
		int total = 0;
		while (!pq.isEmpty()) {
			Edge curEdge = pq.poll();
			if (find(curEdge.a) != find(curEdge.b)) {
				union(curEdge.a, curEdge.b);
				total += curEdge.cost;
				edgeCount++;
			}
			if (edgeCount == (N - 1)) {
				total -= curEdge.cost;
				break;
			}
		}

		System.out.println(total);
	}

	static int find(int x) {
		if (parent[x] == x) return x;
		else parent[x] = find(parent[x]);
		return parent[x];
	}

	static void union(int a, int b) {
		int parentA = find(a);
		int parentB = find(b);

		if (parentA < parentB) {
			parent[parentB] = parentA;
		} else {
			parent[parentA] = parentB;
		}
	}
}