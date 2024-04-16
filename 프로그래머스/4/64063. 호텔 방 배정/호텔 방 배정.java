import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

class Solution {
    static HashMap<Long, Long> roomStatus;
    static List<Long> result;

    public long[] solution(long k, long[] room_number) {
        roomStatus = new HashMap<>();
        result = new ArrayList<>();

        for (long room : room_number) {
            findRoom(room);
        }

        return result.stream().mapToLong(i -> i).toArray();
    }

    long findRoom(long room) {
        if (roomStatus.get(room) == null) {
            roomStatus.put(room, room + 1);
            result.add(room);
            return room + 1;
        } else {
            long enableRoom = findRoom(roomStatus.get(room));
            roomStatus.put(room, enableRoom);
            return enableRoom;
        }
    }
}