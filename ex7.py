def read_numbers():
    numbers = [ int(i) for i in input().split(' ') ]
    return numbers


def num_sum(x):
    sum = 0
    while x > 0:
        sum += x % 10
        x //= 10
    return sum


def good_time(hh, mm):
    hh_sum = num_sum(hh)
    mm_sum = num_sum(mm)
    return hh_sum != mm_sum


def solution(hour, minutes):
    hour.sort()
    minutes.sort()
    retval = []
    for hh in hour:
        for mm in minutes:
            if good_time(hh, mm):
                retval.append('{:02d}:{:02d}'.format(hh, mm))
    return retval


def main():
    hour = read_numbers()
    minutes = read_numbers()
    result = solution(hour, minutes)
    print('\n'.join(result))


main()
