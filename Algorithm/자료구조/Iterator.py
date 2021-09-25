
# class Rainbow:
#     def __init__(self) -> None:
#         self.rainbow=['빨강', '주황', '노랑','초록', '파랑', '남색', '보라']
#         self.index=0

#     def __iter__(self) -> object:
#         return self

#     def __next__(self) -> str:
#         if self.index >= len(self.rainbow): raise StopIteration
#         color=self.rainbow[self.index]
#         self.index+=1
#         return color

# class Semi_Iterator:
#     def __init__(self):
#         self.index=0

#     def __next__(self):
#         print(f'In __next__, index {self.index}')
#         self.index+=1
#         return 0

# class Iterable:
#     def __iter__(self):
#         print(f'call Iterator which contains __next__')
#         return Semi_Iterator()

# iterable=Iterable()
# for i in iterable:
#     pass

# iterator=[1,2,3].__iter__()
# print(iterator.__next__())
# print(iterator.__next__())
# print(iterator.__next__())
# print(iterator.__next__())

print([1,2,3].__iter__())