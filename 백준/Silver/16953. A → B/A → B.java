import java.io.*;
import java.util.*;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int A = Integer.parseInt(st.nextToken());
		int B = Integer.parseInt(st.nextToken());

		System.out.println(bfs(A, B));
	}

	static int bfs(int A, int B) {
		Queue<int[]> q = new LinkedList<>();
		q.add(new int[]{A, 1});

		while (!q.isEmpty()) {
			int curNum = q.peek()[0];
			int count = q.peek()[1];
			q.poll();

			if (curNum == B) return count;
			if (curNum > B) continue;

			q.add(new int[]{curNum * 2, count + 1});
			long i = Long.parseLong(String.valueOf(curNum) + "1");
			if (i > Integer.MAX_VALUE) continue;
			q.add(new int[]{(int) i, count + 1});

		}
		return -1;
	}
}