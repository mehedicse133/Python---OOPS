# Queue Implemene with python oops and list


class Queue:
    def __init__(self):
        self.queue = []

    def push(self, item):
        self.queue.append(item)

    def pop(self):
        if self.is_empty:
            return print("Queue is empty")
        else:
            return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0
        
    def length(self):
        return len(self.queue)   

    def displa_queue_list(self):
        for i in self.queue:
            print(i)


if __name__ == "__main__":
    q = Queue()
    q.push(10)
    q.push(20)
    q.push(30)
    q.displa_queue_list()
    print(q.is_empty())
