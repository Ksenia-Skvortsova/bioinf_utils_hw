# Bioinformatics Utils (HW4)

A packeges developed for processing bioinformatis data. Specifically, it inclides: filtering FASTQ files, converting multiline FASTA sequences into a single-line format and parsing BLAST output to extract the best matches.


## Установка 
To use the packages just clone the repository:

```bash
git clone git@github.com:Ksenia-Skvortsova/bioinf_utils_hw.git
cd bioinf_utils_hw
```

# Functions
## FASTQ-filter
Filters reads on GC-content, length and avereage quality score.

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
## Multiline FASTA to single-line converter
Converts multiline FASTA sequences into a single-line format.

```python
from main_script import convert_fasta

convert_fasta("name_of_your_file.fasta", "output_multiply.fasta")
```

## BLAST-results Parser
Extracts the manes of the best matches from text-based BLAST report and saves them sorted alphabetically.

```python
from main_script parse_blast

parse_blast("name_of_your_BLAST_file.txt", "results_best_hits.fasta")
```

## Requirements
- Python 3.10+
- Python Standart Library

## MEM
![mem](images/Kp3owKAwgcU9nqOurK6JxtlZHlhye5k2lsiNeIoS7AjUSZVEQe2sbMwDQKJCszwarJf4mMw-IIltxdAQ7JDd8Y9xBysUhw.jpg)
