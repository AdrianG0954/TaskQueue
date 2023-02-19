class Task:
    def __init__(self, id, time_left):
        self.id = id
        self.next = None
        self.time_left = time_left
    
    def reduce_time(self, time_to_reduce):
        self.time_left -= time_to_reduce
    
    def __repr__(self):
        return f"id: {self.id}, T_L: {self.time_left})"
    

class TaskQueue:
    def __init__(self, time_per_task=1):
        self.current = None
        self.time_per_task = time_per_task
        self._size = 0
    
    def add_task(self, task):
        if self._size == 0:
            self.current = task
            task.next = task
        else:
            task.next = self.current.next
            self.current.next = task

        self._size += 1
    
    def remove_task(self, task_id):
        if self.is_empty():
            raise RuntimeError("TaskQueue is empty")
        
        current_task = self.current
        for i in range(self._size):
            if current_task.next.id == task_id:
                
                task_to_remove = current_task.next
                current_task.next = task_to_remove.next
                self._size -= 1

                if self._size == 0:
                    self.current = None
                elif self.current.id == task_id:
                    self.current = self.current.next.next

                return task_to_remove
            
            current_task = current_task.next
      

        raise RuntimeError(f"Task with id {task_id} not found")
    
    def is_empty(self):
        return self._size == 0
    
    def __len__(self):
        return self._size
    
    def execute_tasks(self):
        if self.is_empty():
            return 0
        
        total_time = 0
        while self._size > 0:
            task = self.current
            time_to_execute = min(task.time_left, self.time_per_task)
            task.reduce_time(time_to_execute)
            total_time += time_to_execute
            
            if task.time_left <= 0:
                self.remove_task(task.id)
                print(f"Task {task.id} done at {total_time}.")
            else:
                self.current = task.next
                
        return total_time
    
    def __repr__(self):
        if self.is_empty():
            return "TaskQueue()"
        
        ex = []
        current_task = self.current
        for i in range(self._size):
            ex.append(f"id: {current_task.id}, T_L: {current_task.time_left}.")
            current_task = current_task.next
        
        return " -> ".join(ex)


if __name__ == "__main__":
    test = TaskQueue()
    test.add_task(Task(1, 2))
    test.add_task(Task(2, 2))
    test.add_task(Task(3, 2))
    print(test)
    print(test.remove_task(1))
    print(test)
        
