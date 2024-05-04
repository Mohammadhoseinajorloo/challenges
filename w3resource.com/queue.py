# 10. Write a Python program to create a class representing a queue data structure. Include methods for enqueueing and dequeueing elements.
class Queue:
    def __init__(self):
        self.queue = []

    def _isempty(self):
        if len(self.queue) == 0:
            return True
        return False

    def enqueue(self, data):
        return self.queue.append(data)

    def dequeue(self):
        if not self._isempty():
            return self.queue.pop(0)
        raise Exception("Empty!!!")
    
    def front(self):
        if not self._isempty():
            return self.queue[-1]
        raise Exception('Empty!!!')

    def rear(self):
        if not self._isempty():
            return self.queue[0]
        raise Exception('Empty!!!')

    def __repr__(self):
        _str = ''
        for item in self.queue:
            _str += f'[{item}]'
        return _str

if __name__ =='__main__':
    queue = Queue()

