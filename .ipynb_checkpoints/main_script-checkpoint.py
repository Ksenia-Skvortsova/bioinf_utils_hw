import os

from helpers.fastq import (
normalize_bounds, 
read_fastq_records, 
check_gc,
check_length,
check_quality
)

def filter_fastq(
    input_fastq: str,
    output_fastq: str, 
    gc_bounds: tuple[float, float] | float | int = (0, 100), 
    length_bounds: tuple[int, int] | int = (0, 2**32), 
    quality_threshold: float = 0 
) -> None:
    
    """
    Фильтрует FASTQ-файл по GC-составу, длине и среднему качеству.
    Сохраняет отфильтрованные риды в папку 'filtered'.
    
    Аргументы:
        input_fastq: Путь до входного fastq-файла.
        output_fastq: Имя выходного файла.
        gc_bounds:  GC-состав (в процентах).
        length_bounds: Интервал длины для фильтрации.
        quality_threshold: Пороговое значение среднего качества.
    """
    gc_min_max = normalize_bounds(gc_bounds)
    len_min_max = normalize_bounds(length_bounds)
    
    output_dir = "filtered"
    os.makedirs(output_dir, exist_ok=True)
    
    output_path = os.path.join(output_dir, output_fastq)
    
    with open(output_path, 'w') as out_f:
        for header, sequence, plus, quality in read_fastq_records(input_fastq):
            
            if (check_gc(sequence, gc_min_max) and 
                check_length(sequence, len_min_max) and 
                check_quality(quality, quality_threshold)):
                
                out_f.write(f"{header}\n{sequence}\n{plus}\n{quality}\n")