# Bangla Math Evaluator


## Importing the library

```sh
from mathevaluator.benmatheval import Evaluator
```
## Creating instance

```sh
ben_math = Evaluator()
```
## Evaluating

```sh
exp1 = "((৫+৬+৮)/৭*৪-৯%৩)"
new_ex = ben_math.bengali_to_english(exp1)
print(new_ex)

exp2 = "৩*(৩+৬)"
new_ex2 = ben_math.bengali_to_bengali(exp2)
print(new_ex2)
```

License
----

MIT