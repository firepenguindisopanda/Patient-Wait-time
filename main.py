class PatientData:
    def __init__(self, key, value, value2):
        self.key = key
        self.value = value
        self.value2 = value2

    def __repr__(self):
        return f'PatientData({self.key}, {self.value}, {self.value2})'

class DoctorData:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self):
        return f'DoctorData({self.key}, {self.value})'
def parent(i):
    return i // 2

def left_child(i):
    return i * 2

def right_child(i):
    return i * 2 + 1

def swap(arr, i ,j):
    arr[i], arr[j] = arr[j], arr[i]

class Heap:
    def __init__(self):
        self.n = 0
        self.arr = [None]
    def __len__(self):
        return self.n

    def is_empty(self):
        return self.n == 0

    def insert(self, data):
        self.arr.append(data)
        index = len(self.arr) - 1
        self.n += 1
        self._sift_up(index)

    def insert_max(self, data):
        self.arr.append(data)
        index = len(self.arr) - 1
        self.n += 1
        self._sift_up_max(index)

    def _should_move(self, loc, loc2):
        return self.arr[loc].key > self.arr[loc2].key

    def _should_move_max(self, loc, loc2):
        return self.arr[loc].key < self.arr[loc2].key

    def _sift_up(self, index):
        while index > 1 and self._should_move(parent(index), index):
            swap(self.arr, index, parent(index))
            index = parent(index)

    def _sift_up_max(self, index):
        while index > 1 and self._should_move_max(parent(index), index):
            swap(self.arr, index, parent(index))
            index =  parent(index)


    def remove(self):
        index = len(self.arr) - 1
        swap(self.arr, 1, index)
        ans = self.arr.pop(index)
        self._sift_down(1)
        self.n -= 1
        return ans

    def remove_max(self):
        index = len(self.arr) - 1
        swap(self.arr, 1, index)
        ans = self.arr.pop(index)
        self._sift_down_max(1)
        self.n -= 1
        return ans

    def _sift_down_max(self, start):
        curr = start
        n = len(self.arr) - 1
        child_one = left_child(curr)
        while child_one <= n:
            curr_child = child_one
            child_two = right_child(curr)
            if(child_two <= n) and self._should_move_max(child_one, child_two):
                curr_child = child_two
            if(not self._should_move_max(curr, curr_child)):
                break
            swap(self.arr, curr, curr_child)
            curr = curr_child
            child_one = left_child(curr)


    def _sift_down(self, start):
        curr = start
        n = len(self.arr) - 1
        child_one = left_child(curr)
        while child_one <= n:
            curr_child = child_one
            child_two = right_child(curr)
            if(child_two <= n) and self._should_move(child_one, child_two):
                curr_child = child_two
            if(not self._should_move(curr, curr_child)):
                break
            swap(self.arr, curr, curr_child)
            curr = curr_child
            child_one = left_child(curr)

def main():
    filename = 'data.txt'
    filename_two = 'solution.txt'

    patient_heap = Heap()
 
    count = 0
    overall_time = 0
    event_count = 0
    outofbound = []

    fp = open(filename, 'r')
    fp_two = open(filename_two, 'w+')
    for line in fp:
        if event_count > 200:
            break
        else:
            event_code = line[0]
            if event_code == "P":
                count += 1
                event_count += 1
                new_event_code, time, priority = line.split()
                priority = int(priority)
                time = int(time)
                if priority < 0 and priority > 100:
                    data = PatientData(priority, time, new_event_code)
                    outofbound.append(data)
                else:
                    data = PatientData(priority, time, new_event_code)
                    patient_heap.insert_max(data)
            elif event_code == "D":
                event_count += 1
                new_event_code, time = line.split()
                time = int(time)
                data = DoctorData(new_event_code, time)
                removed = patient_heap.remove_max()
                wait_time = data.value - removed.value
                overall_time = overall_time + wait_time

    average_time = overall_time / count

    fp_two.write(str(average_time))
            
    fp.close()
    fp_two.close() 
    
    

if __name__ == '__main__':
    main()
