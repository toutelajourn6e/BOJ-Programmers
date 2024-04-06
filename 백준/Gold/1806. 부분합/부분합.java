import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;


public class Main {
    public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int N = Integer.parseInt(st.nextToken());
		int S = Integer.parseInt(st.nextToken());
		int[] arr = new int[N + 1];

		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < N; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}


		int left = 0, right = 0;
		int window = 0;
		int minLength = Integer.MAX_VALUE;

		while (left <= right && right <= N) {
			if (window >= S && minLength > right - left) minLength = right - left;

			if (window < S) {
				window += arr[right++];
			} else {
				window -= arr[left++];
			}
		}

		if (minLength == Integer.MAX_VALUE) {
            System.out.println(0);
        } else {
            System.out.println(minLength);
        }
	}
}