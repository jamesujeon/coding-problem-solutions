# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    users = {}
    msgs = []
    for cmd in record:
        args = cmd.split()

        if args[0] in ('Enter', 'Change'):
            users[args[1]] = args[2]

        if args[0] == 'Enter':
            msgs.append((args[1], '님이 들어왔습니다.'))
        elif args[0] == 'Leave':
            msgs.append((args[1], '님이 나갔습니다.'))

    return [users[user_id] + msg for user_id, msg in msgs]