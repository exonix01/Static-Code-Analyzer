import os
import sys
import re
import ast


def print_message(n_line, n_message, file_path, name=''):
    msg0 = 'S001 Too long'
    msg1 = 'S002 Indentation is not a multiple of four'
    msg2 = 'S003 Unnecessary semicolon after a statement (note that semicolons are acceptable in comments)'
    msg3 = 'S004 Less than two spaces before inline comments'
    msg4 = 'S005 TODO found (in comments only and case-insensitive)'
    msg5 = 'S006 More than two blank lines preceding a code line (applies to the first non-empty line)'
    msg6 = f'S007 Too many spaces after "{name}" (def or class)'
    msg7 = f'S008 Class name "{name}" should be written in CamelCase'
    msg8 = f'S009 Function name "{name}" should be written in snake_case'
    msg9 = f'S010 Argument name "{name}" should be written in snake_case'
    msg10 = f'S011 Variable "{name}" should be written in snake_case'
    msg11 = 'S012 The default argument value is mutable'
    msg = [msg0, msg1, msg2, msg3, msg4, msg5, msg6, msg7, msg8, msg9, msg10, msg11]
    print(f'{file_path}: Line {n_line}: {msg[n_message - 1]}')


def check_length(n, line, file_path):
    if len(line) > 79:
        print_message(n, 1, file_path)


def check_indentation(n, line, file_path):
    if line[0] == ' ':
        i = 0
        for x in line:
            if x == ' ':
                i += 1
            else:
                if i % 4:
                    print_message(n, 2, file_path)
                break


def check_semicolon(n, line, file_path):
    if line.count(';'):
        for i in line.split():
            if i[0] == '#':
                break
            if i[-1] == ';':
                print_message(n, 3, file_path)


def check_inline_comment(n, line, file_path):
    if line.count('#') and line[0] != '#':
        if line[line.find('#') - 2:line.find('#')] != '  ':
            print_message(n, 4, file_path)


def check_todo(n, line, file_path):
    if line.lower().count('todo') and line.count('#'):
        if line.find('#') < line.lower().find('todo'):
            print_message(n, 5, file_path)


def check_names(n, line, file_path):
    if line.count('class'):
        class_name = line.split()[1]
        if class_name.count('_') or class_name[0].islower():
            print_message(n, 8, file_path, class_name)
        if re.match(r' *class {2,}', line):
            print_message(n, 7, file_path, class_name)
    elif line.count('def'):
        function_name = line.split()[1]
        if not function_name.islower():
            print_message(n, 9, file_path, function_name)
        if re.match(r' *def {2,}', line):
            print_message(n, 7, file_path, function_name)


def check(n, line, file_path):
    check_length(n, line, file_path)
    check_indentation(n, line, file_path)
    check_semicolon(n, line, file_path)
    check_inline_comment(n, line, file_path)
    check_todo(n, line, file_path)
    check_names(n, line, file_path)


def check_argument_names(node, path):
    arguments = node.args.args
    for argument in arguments:
        for letter in argument.arg:
            if letter.isupper():
                print_message(node.lineno, 10, path, argument.arg)


def check_variable_names(node, path):
    for function_body in node.body:
        if not isinstance(function_body, ast.Pass) and isinstance(function_body.value, ast.Name) and not isinstance(
                function_body.targets[0], ast.Attribute):
            variable_name = function_body.targets[0].id
            for letter in variable_name:
                if letter.isupper():
                    print_message(function_body.lineno, 11, path, variable_name)


def check_mutable_arguments(node, path):
    def_args = node.args.defaults
    for def_arg in def_args:
        if isinstance(def_arg, ast.List):
            print_message(node.lineno, 12, path)
            break


def ast_function_check(path):
    file = open(path, 'r')
    code = file.read()
    file.close()
    code_tree = ast.parse(code)
    for node in ast.walk(code_tree):
        if isinstance(node, ast.FunctionDef):
            check_argument_names(node, path)
            check_variable_names(node, path)
            check_mutable_arguments(node, path)


def check_file(path):
    n_blank_lines = 0
    with open(path, 'r') as file:
        for n, line in enumerate(file, start=1):
            check(n, line, path)
            if not line.split():
                n_blank_lines += 1
            elif line.split() and n_blank_lines > 2:
                print_message(n, 6, path)
                n_blank_lines = 0
            else:
                n_blank_lines = 0

    ast_function_check(path)


def main():
    path = str(sys.argv[1])
    if os.path.isdir(path):
        for file in os.listdir(path):
            if file.endswith('.py'):
                check_file(os.path.join(path, file))
    else:
        check_file(path)


if __name__ == '__main__':
    main()
