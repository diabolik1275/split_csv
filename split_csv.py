import csv
import os

def split_csv_with_header(input_file, output_prefix, rows_per_file=4000):
    with open(input_file, 'r', newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        header = next(reader)  # salva l'intestazione

        file_count = 1
        rows = []
        
        for i, row in enumerate(reader, start=1):
            rows.append(row)

            if i % rows_per_file == 0:
                output_file = f'{output_prefix}_{file_count}.csv'
                with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
                    writer = csv.writer(outfile)
                    writer.writerow(header)
                    writer.writerows(rows)
                file_count += 1
                rows = []

        # Scrive l'ultimo file se ci sono righe residue
        if rows:
            output_file = f'{output_prefix}_{file_count}.csv'
            with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
                writer = csv.writer(outfile)
                writer.writerow(header)
                writer.writerows(rows)

    print(f"Suddivisione completata: creati {file_count} file.")

# Esempio d'uso
split_csv_with_header('nome_del_file.csv', 'blocco', rows_per_file=4000)
