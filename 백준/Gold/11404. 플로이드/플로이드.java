
import java.io.*;


public class Main {
	static final int INF = 1_000_000_000;
	static int V, E;
	static int[][] graph;

    public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		V = Integer.parseInt(br.readLine());
		E = Integer.parseInt(br.readLine());
		graph = new int[V + 1][V + 1];

		for (int i = 1; i < V + 1; i++) {
			for (int j = 1; j < V + 1; j++) {
				if (i == j) continue;
				graph[i][j] = INF;
			}
		}

		for (int i = 0; i < E; i++) {
			String[] edgeInfo = br.readLine().split(" ");
			int a = Integer.parseInt(edgeInfo[0]);
			int b = Integer.parseInt(edgeInfo[1]);
			int c = Integer.parseInt(edgeInfo[2]);
			graph[a][b] = Math.min(graph[a][b], c);
		}

		floyd();
	}

	static void floyd() {
		for (int k = 1; k < V + 1; k++) {
			for (int a = 1; a < V + 1; a++) {
				for (int b = 1; b < V + 1; b++) {
					if (a == b) continue;					
					if (graph[a][b] >= graph[a][k] + graph[k][b]) {
						graph[a][b] = graph[a][k] + graph[k][b];
					}

				}
			}
		}

		for (int i = 1; i < V + 1; i++) {
			for (int j = 1; j < V + 1; j++) {
				if (graph[i][j] >= INF) System.out.print(0 + " ");
				else System.out.print(graph[i][j] + " ");
			}
			System.out.println();
		}
	}
}