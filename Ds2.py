from ds import Doublelinkedlist

class stack:
    def __init__(self):
        self.__list = Doublelinkedlist()

    def push(self,val):
        self.__list.add(val)

    def pop(self):
        val = self.__list.back()
        self.__list.remove_last()
        return val

    def is_empty(self):
        return self.__list.size == 0

    def peek(self):
        return self.__list.back()
    def __str__(self):
        return self.__list.size

class Queue:
    def __init__(self):
        self.__list= Doublelinkedlist()

    def enqueue(self,val):
        self.__list.add(val)

    def deque(self):






