from fileTools import FileTools
from view import View
import curses
import curses.ascii


def main(stdscr):
    f = FileTools("/home/mikel/Escritorio")
    title = f.get_current_dir()
    left_title = "hola"
    dirs = sorted(f.current_items())
    view = View(title, dirs)

    while True:
        c = view.main_win.getch()
        if c == ord("q"):
            break
        elif c == curses.KEY_RESIZE:
            view.title_main_window()
            view.render_main_window()
            view.left_title(left_title)
            view.refresh_windows()
            view.dirs_menu(dirs)
        elif c == ord("l"):
            f.change_directory(f.current_dir + "/" + dirs[view.selected])
            title = f.get_current_dir()
            dirs = sorted(f.current_items())
            view.title_main_window(title)
            view.refresh_windows()
            view.dirs_menu(dirs)
            view.selected = 0
        elif c == ord("h"):
            f.change_directory(f.current_dir + "/" + "..")
            title = f.get_current_dir()
            dirs = sorted(f.current_items())
            view.title_main_window(title)
            view.refresh_windows()
            view.dirs_menu(dirs)
            view.selected = 0
        else:
            view.listener(c, dirs)
            view.dirs_menu(dirs)


if __name__ == "__main__":
    curses.wrapper(main)
