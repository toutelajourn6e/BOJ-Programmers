def convert(mel):
    melodies = ['C#', 'D#', 'F#', 'G#','A#']
    change = ['Q', 'W', 'T', 'X', 'Z']
    for idx, melody in enumerate(melodies):
        while melody in mel:
            mel = mel.replace(melody, change[idx])
    return mel
    

def solution(m, musicinfos):
    m = convert(m)
    ans = []
    
    for idx, info in enumerate(musicinfos):
        st, ed, title, mel = info.split(',')
        mel = convert(mel)
        st = ''.join(st.split(':'))
        ed = ''.join(ed.split(':'))

        if st[:2] != ed[:2]:
            playtime = (int(ed) - int(st)) - ((int(ed[:2]) - int(st[:2])) * 40)
        else: playtime = int(ed) - int(st)
        
        if playtime > len(mel):
            matching = mel * (playtime // len(mel)) + mel[:playtime%len(mel)]
        elif playtime < len(mel):
            matching = mel[:playtime]
        else: matching = mel
        
        if m in matching:
            ans.append((playtime, idx, title))

    ans.sort(key=lambda x: (-x[0], x[1]))
    return "(None)" if not ans else ans[0][2]