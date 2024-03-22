import java.io.*;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int N = Integer.parseInt(br.readLine());
		int[] stairs = new int[N];
		int[] d = new int[N];

		for (int i = 0; i < N; i++) {
			stairs[i] = Integer.parseInt(br.readLine());
		}

		switch (N) {
			case 1:
				System.out.println(stairs[0]);
				System.exit(0);
			case 2:
				System.out.println(stairs[0] + stairs[1]);
				System.exit(0);
			case 3:
				System.out.println(Math.max(stairs[0] + stairs[2], stairs[1] + stairs[2]));
				System.exit(0);
			default:
				d[0] = stairs[0];
				d[1] = stairs[0] + stairs[1];
				d[2] = Math.max(stairs[0] + stairs[2], stairs[1] + stairs[2]);
				break;
		}



		for (int i = 3; i < N; i++) {
			d[i] = Math.max((stairs[i] + stairs[i - 1] + d[i - 3]), stairs[i] + d[i - 2]);
		}

		System.out.println(d[N - 1]);
	}
}