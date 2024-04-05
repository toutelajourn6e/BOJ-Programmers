import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;


public class Main {
    public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		int[] arr = new int[N];

		for (int i = 0; i < N; i++) {
			arr[i] = Integer.parseInt(br.readLine());
		}

		Arrays.sort(arr);

		int left = 0, right = 0;
		int result = Integer.MAX_VALUE;

		while (left < N && right < N) {
			int different = arr[right] - arr[left];
			if (different < M) {
				right++;
			} else {
				result = Math.min(result, different);
				left++;
			}
		}

		System.out.println(result);
	}
}