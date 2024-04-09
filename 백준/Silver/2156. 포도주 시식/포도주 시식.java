import java.io.*;


public class Main {
    public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int N = Integer.parseInt(br.readLine());
		int[] wine = new int[N + 1];

		for (int i = 1; i <= N; i++) {
			wine[i] = Integer.parseInt(br.readLine());
		}

		if (N == 1) {
			System.out.println(wine[1]);
			return;
		}

		int[] dp = new int[N + 1];
		dp[1] = wine[1];
		dp[2] = wine[1] + wine[2];

		for (int i = 3; i <= N; i++) {
			dp[i] = dp[i - 1];
			dp[i] = Math.max(dp[i], dp[i - 2] + wine[i]);
			dp[i] = Math.max(dp[i], dp[i - 3] + wine[i - 1] + wine[i]);
		}

		System.out.println(dp[N]);
	}
}