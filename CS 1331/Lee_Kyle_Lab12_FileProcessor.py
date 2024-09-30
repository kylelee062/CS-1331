import csv

class FileProcessor:
    
    def merge(file1_path, file2_path, result_path):
        try:
            with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2, open(result_path, 'w') as result_file:
                result_file.write(file1.read())
                result_file.write(file2.read())
                print("Merged! Result written as", result_path)
        except FileNotFoundError as e:
            print("Error:", e)
        except Exception as e:
            print("Error during merge:", e)

    def copy(file1_path, num_copies):
        try:
            with open(file1_path, 'r') as original_file:
                file_content = original_file.read()
                for i in range(num_copies):
                    copy_open = file1_path.replace('.txt', f'_copy{i+1}.txt')
                    with open(copy_open, 'w') as copy_file:
                        copy_file.write(file_content)
            print(f"{num_copies} copies of {file1_path} succesfully copied.")
        except FileNotFoundError as e:
            print("Error:", e)
        except Exception as e:
            print("Error during copy:", e)

    def convert_to_csv(text_file_path, csv_file_path):
        try:
            with open(text_file_path, 'r') as text_file, open(csv_file_path, 'w') as csv_file:
                csv_writer = csv.writer(csv_file)
                for line in text_file:
                    modified_line = line.replace(' ', ',')
                    # csv_writer.writerow([modified_line])
                    csv_file.write(modified_line)
            print("Converted! Result written as", csv_file_path)
        except FileNotFoundError as e:
            print("Error:", e)
        except Exception as e:
            print("Error during conversion:", e)


    def file_statistics(file_path):
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
                words = sum(len(line.split()) for line in lines)
                print(f"Number of lines: {len(lines)}")
                print(f"Number of words: {words}")
        except FileNotFoundError as e:
            print("Error:", e)
        except Exception as e:
            print("Error during file statistics:", e)
