import java.io.*;
import java.util.StringTokenizer;


public class Main {
    public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		final int R = 0, G = 1, B = 2;
		int N = Integer.parseInt(br.readLine());
		int[][] costs = new int[N][3];
		int[][] dp = new int[3][N];

		for (int i = 0; i < N; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			costs[i][R] = Integer.parseInt(st.nextToken());
			costs[i][G] = Integer.parseInt(st.nextToken());
			costs[i][B] = Integer.parseInt(st.nextToken());
		}

		dp[R][0] = costs[0][R];
		dp[G][0] = costs[0][G];
		dp[B][0] = costs[0][B];

		for (int i = 1; i < N; i++) {
			dp[R][i] = Math.min(dp[G][i - 1], dp[B][i - 1]) + costs[i][R];
			dp[G][i] = Math.min(dp[R][i - 1], dp[B][i - 1]) + costs[i][G];
			dp[B][i] = Math.min(dp[R][i - 1], dp[G][i - 1]) + costs[i][B];
		}

		int tmp = Math.min(dp[R][N - 1], dp[G][N - 1]);
		System.out.println(Math.min(tmp, dp[B][N - 1]));
	}
}