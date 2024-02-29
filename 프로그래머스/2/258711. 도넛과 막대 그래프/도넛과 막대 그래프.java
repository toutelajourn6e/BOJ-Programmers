import java.util.*;

class Solution {
    public int[] solution(int[][] edges) {
        HashMap<Integer, int[]> graph = new HashMap<>();
        int created = 0, donut = 0, stick = 0, eight = 0;
        
        for (int[] edge : edges) {
            if (graph.get(edge[0]) == null) {
                graph.put(edge[0], new int[]{0, 0});
            }
            if (graph.get(edge[1]) == null) {
                graph.put(edge[1], new int[]{0, 0});
            }
            graph.get(edge[0])[1] += 1; // Output + 1
            graph.get(edge[1])[0] += 1; // Input + 1
        }
        
        int totalGraphCount = 0;
        
        Set<Integer> key = graph.keySet();
        for (int node : key) {
            int in = graph.get(node)[0];
            int out = graph.get(node)[1];

            if (in >= 1 && out == 0) {
                stick += 1;
            } else if (in >= 2 && out == 2) {
                eight += 1;
            } else if (in == 0 && out >= 2) {
                created = node;
                totalGraphCount = out;
            }
        }

        
        return new int[]{created, totalGraphCount - (stick + eight), stick, eight};
    }
}