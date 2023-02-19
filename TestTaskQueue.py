import unittest
from TaskQueue import *

class TestTaskQueue(unittest.TestCase):
    
    def test_taskInit(self):
        test = Task(1, 2)
        self.assertEqual(test.id, 1)
        self.assertEqual(test.time_left, 2)
        self.assertEqual(test.next, None)


    def test_taskReduceTime(self):
        test = Task(1, 2)
        test.reduce_time(1)
        self.assertEqual(test.time_left, 1)

    def test_TaskQInit(self):
        test = TaskQueue()
        self.assertEqual(test.current, None)
        self.assertEqual(test.time_per_task, 1)
        self.assertEqual(test._size, 0)

        test2 = TaskQueue(2)
        self.assertEqual(test2.time_per_task, 2)

    def test_taskQadd(self):
        test = TaskQueue()
        test.add_task(Task(1, 2))
        self.assertEqual(test.current.id, 1)
        self.assertEqual(test.current.next, test.current)
        self.assertEqual(test._size, 1)

        test2 = TaskQueue()
        test2.add_task(Task(1, 2))
        test2.add_task(Task(2, 2))
        self.assertEqual(test2.current.next.id, 2)
        self.assertEqual(test2.current.next.next, test2.current)

    def test_taskQremove(self):
        test = TaskQueue()
        test.add_task(Task(1, 2))
        test.add_task(Task(2, 2))
        test.add_task(Task(3, 2))

    
        test.remove_task(3)
        self.assertEqual(test.current.next.id, 2)

        
        test.remove_task(1)
        self.assertEqual(test.current.id, 2)

        
        test.remove_task(2)
        self.assertEqual(test.current, None)

    def test_taskQis_empty(self):
        test = TaskQueue()
        self.assertEqual(test.is_empty(), True)

        test.add_task(Task(1, 2))
        self.assertEqual(test.is_empty(), False)

    def test_taskQlen(self):
        test = TaskQueue()
        self.assertEqual(test.__len__(), 0)

        test.add_task(Task(1, 2))
        self.assertEqual(test.__len__(), 1)

        test.add_task(Task(2, 2))
        self.assertEqual(test.__len__(), 2)

        test.remove_task(1)
        self.assertEqual(test.__len__(), 1)

        test.remove_task(2)
        self.assertEqual(test.__len__(), 0)

    def test_taskQexecuteTasks(self):
        test = TaskQueue()
        test.add_task(Task(1, 2))
        test.add_task(Task(2, 2))
        test.add_task(Task(3, 2))

        self.assertEqual(test.execute_tasks(), 6)
        self.assertEqual(test.current, None)


if (__name__ == "__main__"):    
    unittest.main()




