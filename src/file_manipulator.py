import sys
import os


def read_file(file_path: str) -> str:
    # ファイルが存在するか確認して内容を返す
    if not os.path.isfile(file_path):
        print(f"Error: File not found: {file_path}")
        sys.exit(1)
    try:
        with open(file_path, 'r') as f:
            return f.read()
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        sys.exit(1)


def write_file(file_path: str, content: str) -> None:
    # ファイルに内容を書き込む
    try:
        with open(file_path, 'w') as f:
            f.write(content)
    except Exception as e:
        print(f"Error writing file {file_path}: {e}")
        sys.exit(1)


def reverse_operation(input_path: str, output_path: str) -> None:
    # ファイル内容を逆順にして出力
    write_file(output_path, read_file(input_path)[::-1])


def copy_operation(input_path: str, output_path: str) -> None:
    # ファイル内容をコピー
    write_file(output_path, read_file(input_path))


def duplicate_contents_operation(input_path: str, n: int) -> None:
    # ファイル内容をn回繰り返して書き込む
    content = read_file(input_path)
    write_file(input_path, content * n)


def replace_string_operation(input_path: str, old: str, new: str) -> None:
    # ファイル内の文字列を置換
    content = read_file(input_path)
    write_file(input_path, content.replace(old, new))


def is_valid_args(argv):
    # 引数の数が操作に対して正しいかチェック
    operations_args_count = {
        "reverse": 4,
        "copy": 4,
        "duplicate-contents": 4,
        "replace-string": 5,
    }
    if len(argv) < 2:
        return False
    expected = operations_args_count.get(argv[1])
    return expected is not None and len(argv) == expected


def print_usage():
    # CLIの使い方を表示
    print("---------------")
    print("Usage:")
    print("  reverse input_file output_file")
    print("  copy input_file output_file")
    print("  duplicate-contents input_file times")
    print("  replace-string input_file old new")
    print("---------------")


def main():
    argv = sys.argv
    if not is_valid_args(argv):
        print_usage()
        sys.exit(1)

    operation = argv[1]
    try:
        if operation == "reverse":
            reverse_operation(argv[2], argv[3])
        elif operation == "copy":
            copy_operation(argv[2], argv[3])
        elif operation == "duplicate-contents":
            duplicate_contents_operation(argv[2], int(argv[3]))
        elif operation == "replace-string":
            replace_string_operation(argv[2], argv[3], argv[4])
    except ValueError:
        print("Error: Invalid value for integer argument")
        sys.exit(1)


if __name__ == "__main__":
    main()
