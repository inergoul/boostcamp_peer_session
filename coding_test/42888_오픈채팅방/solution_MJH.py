def solution(record):
    user_id = {EC.split()[1]:EC.split()[-1] for EC in record if EC.startswith('Enter') or EC.startswith('Change')}
    return [f'{user_id[E_L.split()[1]]}님이 들어왔습니다.' if E_L.startswith('Enter') else f'{user_id[E_L.split()[1]]}님이 나갔습니다.' for E_L in record if not E_L.startswith('Change')]
