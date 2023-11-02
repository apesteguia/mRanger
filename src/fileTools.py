from ast import List
import os


class FileTools:
    def __init__(self, rootDir: str = ""):
        self.dir_items: List = []
        self.sub_dir_items: List = []
        self.file_content: str = ""
        if not rootDir:
            self.current_dir = os.getcwd()
        else:
            if os.path.exists(rootDir) and os.path.isdir(rootDir):
                self.current_dir = rootDir
            else:
                raise ValueError(
                    "The specified root directory does not exist or is not a directory."
                )

    def get_current_dir(self):
        return self.current_dir

    def change_directory(self, path):
        try:
            if os.path.exists(path) and os.path.isdir(path):
                os.chdir(path)
                self.current_dir = os.getcwd()
            else:
                raise FileNotFoundError(
                    f"The specified directory '{path}' does not exist or is not a directory."
                )
        except Exception as e:
            raise e

    def get_file_contents(self, path: str):
        if not path:
            self.file_content = ""
        else:
            if os.path.exists(path) and os.path.isfile(path):
                with open(path, "r") as file:
                    self.file_content = file.read()
            else:
                raise FileNotFoundError(f"The specified file '{path}' does not exist.")
        return self._file_content

    def current_items(self):
        if not self.current_dir:
            self.dir_items = []
        else:
            if os.path.exists(self.current_dir) and os.path.isdir(self.current_dir):
                self.dir_items = [item for item in os.listdir(self.current_dir)]
            else:
                raise FileNotFoundError(
                    f"The specified directory '{self.current_dir}' does not exist or is not a directory."
                )
        return self.dir_items

    def current_folders(self):
        if not self.current_dir:
            self.dir_items = []
        else:
            if os.path.exists(self.current_dir) and os.path.isdir(self.current_dir):
                self.dir_items = [
                    d
                    for d in os.listdir(self.current_dir)
                    if os.path.isdir(os.path.join(self.current_dir, d))
                ]
            else:
                raise FileNotFoundError(
                    f"The specified directory '{self.current_dir}' does not exist or is not a directory."
                )
        return self.dir_items

    def secondary_folders(self, path: str):
        if not path:
            self.sub_dir_items = []
        else:
            if os.path.exists(path) and os.path.isdir(path):
                self.sub_dir_items = [
                    d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))
                ]
            else:
                raise FileNotFoundError(
                    f"The specified directory '{path}' does not exist or is not a directory."
                )
        return self.sub_dir_items
