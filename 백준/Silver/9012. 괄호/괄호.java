import java.io.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());

		for (int i = 0; i < N; i++) {
			String result = "NO";
			int stack = 0;
			String ps = br.readLine();

			for (int j = 0; j < ps.length(); j++) {
				char c = ps.charAt(j);
				if (c == '(') {
					stack++;
				} else if (c == ')' && stack > 0) {
					stack--;
				} else {
					stack = -1;
					break;
				}
			}

			if (stack == 0) result = "YES";
			System.out.println(result);
		}
	}
}