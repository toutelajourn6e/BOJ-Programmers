import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class Main {
	public static int[] parent;
	public static boolean[] visited;
	public static List<List<Integer>> edges = new ArrayList<>();

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();

		int N = Integer.parseInt(br.readLine());
		parent =  new int[N + 1];
		visited = new boolean[N + 1];


		for (int i = 0; i < N+1; i++) {
			edges.add(new ArrayList<Integer>());
		}

		for (int i = 0; i < N-1; i++) {
			String[] edgeInfo = br.readLine().split(" ");
			int A = Integer.parseInt(edgeInfo[0]);
			int B = Integer.parseInt(edgeInfo[1]);
			edges.get(A).add(B);
			edges.get(B).add(A);
		}

		search(1);

		for (int i = 2; i < parent.length; i++) {
			sb.append(parent[i] + "\n");
		}

		System.out.println(sb);
	}

	public static void search(int curNode) {
		for (int nextNode : edges.get(curNode)) {
			if (!visited[nextNode]) {
				visited[nextNode] = true;
				parent[nextNode] = curNode;
				search(nextNode);
			}
		}
	}
}