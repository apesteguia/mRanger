import curses
from fileTools import FileTools
from view import View

def main(stdscr):
    f = FileTools("/home/mikel")
    title = f.get_current_dir()
    view = View(title)

    view.render(title)

if __name__ == "__main__":
    curses.wrapper(main)
