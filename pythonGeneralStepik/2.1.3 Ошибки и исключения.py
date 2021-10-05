class EvenLengthMixin:
    def even_length(self):
        return len(self) % 2 == 0


class MyList(list, EvenLengthMixin):
    pass


ml = MyList([1, 2, 3, 4])
ml.sort()
print(ml)