def add_text_and_print_selected(content, file_path):
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(content + '\n')

    with open(file_path, 'r', encoding='utf-8') as file:
        all_lines = file.readlines()
        for index, current_line in enumerate(all_lines):
            if index % 2 != 0:
                print(current_line.rstrip())

add_text_and_print_selected("Новая строка", "data.txt")
#add_text_and_print_selected("Еще одна строка", "data.txt")
#add_text_and_print_selected("И последняя строка", "data.txt")
