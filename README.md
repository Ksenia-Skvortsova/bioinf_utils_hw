# Bioinformatics Utils (HW4)

Пакеты, разработанные для обработки биоинформатических данных, в частности: фильтрация fastq-файлов,преобразование строк в fasta-файле в одну длинную строку и отбор данных результатов BLASTA по наилучшим совпадениям. 


## Установка 
Для использования пакетов достаточно склонировать репозиторий: 

```bash
git clone git@github.com:Ksenia-Skvortsova/bioinf_utils_hw.git
cd bioinf_utils_hw
```

# Функции
## FASTQ-фильтратор.
Функция фильтрует риды по GC-составу, длине и среднему качеству прочтения. Сохраняет отфильтрованные данные в папку filtered.

```python
from main_script import filter_fasrq

filter_fastq(
    input_fastq = "name_your_file.fastq",
    output_fastq = "name_output_dir", 
    gc_bounds = (40,60), 
    length_bounds = (50,100), 
    quality_threshold = 20 
)
```
## Конвертарция в многострочный FASTA-файл
Преобразует многострочные последовательности в однострочный формат.

```python
from main_script import convert_fasta

convert_fasta("name_of_your_file.fasta", "output_multiply.fasta")
```

## Отбор BLAST-результатов
Извлекает названия лучших совпадений из текстового отчета BLAST и сохраняет их отсортированными по алфавиту. 

```python
from main_script parse_blast

parse_blast("name_of_your_BLAST_file.txt", "results_best_hits.fasta")
```

## Требования 
- Python 3.10+
- Стандартная библиотека Python

## MEM
![mem](images/Kp3owKAwgcU9nqOurK6JxtlZHlhye5k2lsiNeIoS7AjUSZVEQe2sbMwDQKJCszwarJf4mMw-IIltxdAQ7JDd8Y9xBysUhw.jpg)
