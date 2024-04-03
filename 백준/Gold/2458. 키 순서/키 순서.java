import java.io.*;


public class Main {
	static int V, E;
	static boolean[][] graph;

    public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		String[] graphInfo = br.readLine().split(" ");
		V = Integer.parseInt(graphInfo[0]);
		E = Integer.parseInt(graphInfo[1]);
		graph = new boolean[V + 1][V + 1];

		for (int i = 0; i < E; i++) {
			String[] edgeInfo = br.readLine().split(" ");
			int a = Integer.parseInt(edgeInfo[0]);
			int b = Integer.parseInt(edgeInfo[1]);
			graph[a][b] = true;
		}

		floyd();
	}

	static void floyd() {
		for (int k = 1; k < V + 1; k++) {
			for (int a = 1; a < V + 1; a++) {
				for (int b = 1; b < V + 1; b++) {
					if (graph[a][k] && graph[k][b]) {
						graph[a][b] = true;
					}
				}
			}
		}

		int[] cnt = new int[V + 1];
		for (int i = 1; i < V + 1; i++) {
			for (int j = 1; j < V + 1; j++) {
				if (graph[i][j] || graph[j][i]) cnt[i]++;
			}
		}

		int result = 0;
		for (int i = 1; i < cnt.length; i++) {
			if (cnt[i] == V - 1) result++;
		}
		System.out.println(result);
	}
}