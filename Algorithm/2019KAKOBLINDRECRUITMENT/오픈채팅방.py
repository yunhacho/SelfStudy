def solution(record):
    log, ID, m = [], {}, {'E': '님이 들어왔습니다.', 'L':'님이 나갔습니다.'}
    for r in record:
        act, *info = r.split()
        if act[0]=='E': ID[info[0]]=info[1]; log.append(('E', info[0]))
        elif act[0]=='L': log.append(('L', info[0]))
        else: ID[info[0]]=info[1]
    return [ID[id]+m[act] for act, id in log]