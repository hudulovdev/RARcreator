import rarfile

def create_rar(file_paths, output_file):
    with rarfile.RarFile(output_file, 'w') as archive:
        for file_path in file_paths:
            archive.write(file_path)

# Example usage:
file_paths = ['file1.txt', 'file2.txt', 'file3.txt']
output_file = 'archive.rar'

create_rar(file_paths, output_file)
