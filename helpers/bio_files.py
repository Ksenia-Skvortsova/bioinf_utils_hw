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