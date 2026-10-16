import os

def convert_multiline_fasta_to_oneline(input_fasta: str, output_fasta: str)-> None:
    """
    Преобразует многострочный fasta-файл в однострочный формат.
    
    Аргументы:
        input_fasta: Путь до входного fasta-файла.
        output_fasta: Путь до выходного fasta-файла.
    """
    current_head = None
    current_seq = ""
    with open(input_fasta, 'r') as infile, open(output_fasta, 'w') as outfile: 
        for line in infile:
            line = line.strip()
            
            if line.startswith(">"):
                if current_head is not None: 
                    outfile.write(f"{current_head}\n{current_seq}\n")
                current_head = line
                current_seq = ""
            else: 
                current_seq += line
        if current_head is not None: 
            outfile.write(f"{current_head}\n{current_seq}\n")

def parse_blast_output(input_file: str, output_file: str) -> None: 
    """
    Парсит вывод BLAST, извлекает лучшие совпадения и сохраняет их в файл.
    
    Аргументы:
        input_file: Путь до входного файла с результатами BLAST (.txt).
        output_file: Путь до выходного файла для сохранения названий.
    """
    best_hits = []
    with open(input_file, 'r') as infile:
        for line in infile:
            line = line.strip()

            if line.startswith("Sequences producing significant alignments:"):
                infile.readline()
                infile.readline()
                first_result_line = infile.readline().strip()
                if first_result_line:
                    best_hits.append(first_result_line)
    best_hits.sort()

    with open(output_file, 'w') as outfile: 
        for name in best_hits:
            outfile.write(f"{name}\n")