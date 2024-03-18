import java.io.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();

		int[] dwarfs = new int[9];
		int sum = 0;

		for (int i = 0; i < 9; i++) {
			int num = Integer.parseInt(br.readLine());
			dwarfs[i] = num;
			sum += num;
		}

		for (int i = 0; i < 9; i++) {
			for (int j = i+1; j < 9; j++) {
				if (sum - (dwarfs[i] + dwarfs[j]) == 100) {
					for (int k = 0; k < 9; k++) {
						if (k != i && k != j) {
							sb.append(dwarfs[k] + "\n");
						}
					}
				}
			}
		}

		System.out.println(sb);

	}
}