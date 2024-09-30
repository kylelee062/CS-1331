from Lee_Kyle_Lab12_FileProcessor import FileProcessor

def main():
    FileProcessor.merge('file1.txt', 'file2.txt', 'result.txt')
    FileProcessor.copy('file1.txt', 3)
    FileProcessor.convert_to_csv('file1.txt', 'csv_file.csv')
    FileProcessor.file_statistics('file1.txt')

if __name__ == "__main__":
    main()
