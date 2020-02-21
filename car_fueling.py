# python3
import sys

def compute_min_refills(distance, tank, stops):
    # write your code here
    number_stops = 0
    distance_travel = 0
    stops.append(distance)
    #[y-x for x,y in pairwise(a)]
    difference = [t - s for s, t in zip(stops, stops[1:])]

    if any(i > tank for i in difference):
        return -1

    for i in range(len(stops)):
        if i < len(stops) - 1:
            value1 = tank - (stops[i] - distance_travel)
            value2 = tank - (stops[i+1] - distance_travel)
            if (value1 >= 0) and (value2 < 0):
                number_stops += 1
                distance_travel = stops[i]
    return number_stops

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
