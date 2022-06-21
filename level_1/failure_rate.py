# programmers level1 - failure rate

def stage_check(stage_list, check_s):
    pass_list = []
    fail_list = []

    for stage in stage_list:
        if stage > check_s:
            pass_list.append(stage)
        else:
            fail_list.append(stage)

    return pass_list, fail_list


def solution(N, stages):
    pass_list = stages
    fail_list = []
    fail_rate = []

    for curr_stage in range(1, N + 1):
        total = len(pass_list)
        pass_list, fail_list = stage_check(pass_list, curr_stage)
        fail_rate.append((len(pass_list) + 0.0001) / (total + 0.0001))

    result_temp = sorted(range(len(fail_rate)), key=lambda k: fail_rate[k], reverse=False)
    result = [x + 1 for x in result_temp]

    return result
