from collections import defaultdict

def solution(genres, plays):
    genre_best = defaultdict(list)
    genre_cnt = defaultdict(int)
    result = []
    
    for index, music in enumerate(zip(genres, plays)):
        genre, play = music
        genre_cnt[genre] += play
        genre_best[genre].append((index, play))
        
    for genre, _ in sorted(genre_cnt.items(), key=lambda x: -x[1]):
        for idx, _ in sorted(genre_best[genre], key=lambda x: -x[1])[:2]:
            result.append(idx)
            
    return result