from collections import defaultdict

def solution(genres, plays):
    genre_best = defaultdict(list)
    genre_cnt = defaultdict(int)
    result = []
    
    for index, music in enumerate(zip(genres, plays)):
        genre, play = music
        genre_cnt[genre] += play
        genre_best[genre].append((index, play))
        
    for genre in genre_best:
        genre_best[genre].sort(key=lambda x: (-x[1], x[0]))
    
    temp = []
    for genre in genre_cnt:
        temp.append((genre, genre_cnt[genre]))
    
    temp.sort(key=lambda x: -x[1])
    
    for genre, cnt in temp:
        if len(genre_best[genre]) >= 2:
            result.append(genre_best[genre][0][0])
            result.append(genre_best[genre][1][0])
        else:
            result.append(genre_best[genre][0][0])
                
        
    return result