import java.io.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		String roomNumber = br.readLine();
		int[] numCount = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};


		for (char c : roomNumber.toCharArray()) {
			int num = Character.getNumericValue(c);
			numCount[num]++;
		}

		numCount[6] = (int) Math.ceil((double) (numCount[9] + numCount[6]) / 2);
		int maxNum = 0;

		for (int i = 0; i < numCount.length - 1; i++) {
			maxNum = Math.max(numCount[i], maxNum);
		}
		System.out.println(maxNum);

		br.close();
	}
}