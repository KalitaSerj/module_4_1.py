from fake_math import divide as fm
from true_math import divide as tm

fake = fm(8, 0)
true = tm(8, 0)

print("Результат деления fake_math:", fake)
print("Результат деления true_math:", true)
