if __name__ == "__main__":
    n = int(input())
    arr = map(int, input().split())

    array_list = list(set(arr))
    array_list.sort()

    outcome = array_list[-2]
    print(outcome)
