import java.io.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int A = Integer.parseInt(br.readLine());
		int B = Integer.parseInt(br.readLine());
		int C = Integer.parseInt(br.readLine());

		if (A + B + C == 180) {
			if (A == B && B == C) {
				bw.write("Equilateral");
			} else if (A != B && B != C && C != A) {
				bw.write("Scalene");
			} else {
				bw.write("Isosceles");
			}
		} else {
			bw.write("Error");
			bw.flush();
		}
		bw.flush();
		br.close();
		bw.close();
	}
}