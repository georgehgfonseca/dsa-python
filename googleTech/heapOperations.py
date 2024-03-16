import heapq

def insert_to_heap(heap, value):
    heapq.heappush(heap, value)
    
def delete_from_heap(heap, value):
    to_add_back = []
    while True:
        min_val = heapq.heappop(heap)
        if min_val == value:
            break
        to_add_back.append(min_val)

    for elem in to_add_back:
        insert_to_heap(heap, value)

def print_minimum(heap):
    min_val = heapq.heappop(heap)
    print(min_val)
    insert_to_heap(heap, min_val)



if __name__=='__main__':
    num_test_cases = int(input())
    heap = []
    for _ in range(num_test_cases):
        test_case_data = list(map(int, input().strip().split()))
        # print(test_case_data)

        if test_case_data[0] == 1:
            insert_to_heap(heap, test_case_data[1])

        elif test_case_data[0] == 2:
            delete_from_heap(heap, test_case_data[1])

        elif test_case_data[0] == 3:
            print_minimum(heap)
