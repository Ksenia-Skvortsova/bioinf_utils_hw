import os 

# функция для подсчета GC-состава
def calculate_gc_content(sequence: str) -> float:
    """
    Вычисляет процент GC-состава в последовательности.
    
    Аргументы:
        sequence: Строка с нуклеотидной последовательностью.
        
    Returns:
        float: Процент GC (от 0.0 до 100.0).
    """
    seq_upper = sequence.upper()
    gc_count = seq_upper.count('G') + seq_upper.count('C')
    return (gc_count / len(sequence))*100.0

    
#функция которая считает среднее качество
def calculate_avg_quality(quality_str: str) -> float:
    """
    Вычисляет среднее качество ридов по шкале Phred33.
    
    Аргументы:
        quality_str: Строка с символами качества (4-я строка FASTQ).
        
    Returns:
        float: Среднее значение качества. Возвращает 0.0, если строка пустая.
    """
    total_quality = sum(ord(char) - 33 for char in quality_str)
    return total_quality / len(quality_str)


# функция котрая преправщает число в кортеж
def normalize_bounds(bounds: tuple[float, float] | float | int) -> tuple[float, float]:
    """
    Приводит границы интервала к единому формату кортежа (lower, upper).
    
    Аргументы:
        bounds: Кортеж из двух чисел или одно число.
        
    Returns:
        tuple[float, float]: Кортеж из двух чисел (lower_bound, upper_bound).
    """
    if isinstance(bounds, tuple):
        return bounds
    else:
        return (0.0, float(bounds))
    

# функция для оптимизации памяти, читает файл по 4 строки
def read_fastq_records(file_path: str):
    """
    Функция для построчного чтения FASTQ файла.
    Возвращает кортежи (header, sequence, plus, quality) по одному риду за раз.
    Поможет сэкономить оперативную память, тк не будет загружать весь файл сразу
    
    Аргументы:
        file_path: Путь к входному FASTQ файлу.
        
    Yields:
        tuple: (header, sequence, plus, quality)
    """
    with open(file_path, 'r') as f: 
        while True: 
            header = f.readline().strip()
            if not header:
                break
            sequence = f.readline().strip()
            plus = f.readline().strip()
            quality = f.readline().strip()
            yield header, sequence, plus, quality


# функции-проверки
def check_gc(sequence: str, bounds: tuple[float, float]) -> bool:
    """
    Проверяет, находится ли GC-состав последовательности в заданных границах.
    
    Аргументы:
        sequence: Строка с нуклеотидной последовательностью.
        bounds: Кортеж (min_gc, max_gc).
        
    Returns:
        bool: True, если GC-состав в границах, иначе False.
    """
    gc_content = calculate_gc_content(sequence)
    return bounds[0] <= gc_content <= bounds[1]


def check_length(sequence: str, bounds: tuple[float, float]) -> bool: 
    """
    Проверяет, находится ли длина последовательности в заданных границах.
    
    Аргументы:
        sequence: Строка с нуклеотидной последовательностью.
        bounds: Кортеж (min_length, max_length).
        
    Returns:
        bool: True, если длина в границах, иначе False.
    """
    length = len(sequence)
    return bounds[0] <= length <= bounds[1]


def check_quality(quality_str: str, threshold: float) -> bool:
    """
    Проверяет, превышает ли среднее качество пороговое значение.
    
    Аргументы:
        quality_str: Строка с символами качества.
        threshold: Пороговое значение качества.
        
    Returns:
        bool: True, если качество >= threshold, иначе False.
    """
    avg_quality = calculate_avg_quality(quality_str)
    return avg_quality >= threshold