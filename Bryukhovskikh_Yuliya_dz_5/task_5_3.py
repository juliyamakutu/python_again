from typing import Generator, List, Tuple


tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Юлия', 'Юлёна']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']


def check_gen(tutors: List[str], klasses: List[str]) -> Generator[Tuple[str], None, None]:
    for i in range(len(tutors)):
        tutor = tutors[i]
        if i < len(klasses):
            klass = klasses[i]
        else:
            klass = None
        yield (tutor, klass)


generator = check_gen(tutors, klasses)
# добавьте здесь доказательство, что создали именно генератор
print(f'тип результата: {type(check_gen(tutors, klasses))}')
for _ in range(len(tutors)):
    print(next(generator))
# next(generator)  # если раскомментировать, то должно падать в traceback по StopIteration