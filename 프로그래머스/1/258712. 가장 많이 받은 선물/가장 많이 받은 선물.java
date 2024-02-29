import java.util.*;

class Solution {
    public int solution(String[] friends, String[] gifts) {
        HashMap<String, HashMap<String, Integer>> giftRelation = new HashMap<>();
        HashMap<String, Integer> giftPoint = new HashMap<>();
        HashMap<String, Integer> count = new HashMap<>();
        
        for (String friend : friends) {
            giftRelation.put(friend, new HashMap<String, Integer>());
        }
        
        for (String gift : gifts) {
            String[] info = gift.split(" ");
            String sender = info[0];
            String receiver = info[1];
            
            giftRelation.get(sender).put(receiver, giftRelation.get(sender).getOrDefault(receiver, 0) + 1);
            giftRelation.get(receiver).put(sender, giftRelation.get(receiver).getOrDefault(sender, 0) - 1);
            
            giftPoint.put(sender, giftPoint.getOrDefault(sender, 0) + 1);
            giftPoint.put(receiver, giftPoint.getOrDefault(receiver, 0) - 1);
                  
        }
        
        for (int i = 0; i < friends.length-1; i++) {
            for (int j = i+1; j < friends.length; j++) {
                int pointI = giftRelation.get(friends[i]).getOrDefault(friends[j], 0);
                int pointJ = giftRelation.get(friends[j]).getOrDefault(friends[i], 0);
                
                if (pointI > pointJ) {
                    count.put(friends[i], count.getOrDefault(friends[i], 0) + 1);
                } else if (pointI < pointJ) {
                    count.put(friends[j], count.getOrDefault(friends[j], 0) + 1);
                } else {
                    int giftPointI = giftPoint.getOrDefault(friends[i], 0);
                    int giftPointJ = giftPoint.getOrDefault(friends[j], 0);
                    if (giftPointI > giftPointJ) {
                        count.put(friends[i], count.getOrDefault(friends[i], 0) + 1);
                    } else if (giftPointI < giftPointJ) {
                        count.put(friends[j], count.getOrDefault(friends[j], 0) + 1);
                    }
                }
            }
        }
        count.put("equal", 0);
        return Collections.max(count.values());
    }
}