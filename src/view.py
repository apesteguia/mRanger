import curses

class View:
    def __init__(self, title: str):
        self.main_win = curses.initscr()
        curses.curs_set(0)
        curses.start_color()
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_BLUE , curses.COLOR_BLACK)
        self.main_win.bkgd(curses.color_pair(1))

        self.render_main_window(title)
        self.refresh_windows("hola")

    def render_main_window(self, title: str):
        self.main_win.clear()
        self.main_win.box()
        self.main_win.addstr(0, 1, title, curses.A_BOLD)
        self.main_win.refresh()

    def refresh_windows(self, title: str):
        height, width = self.main_win.getmaxyx()
        window_height = height - 2
        window_width = width // 2

        self.left_win = self.main_win.subwin(window_height, window_width, 1, 0)
        self.right_win = self.main_win.subwin(window_height, window_width, 1, window_width)

        self.left_win.clear()
        self.left_win.box()
        #self.left_win.addstr(0, 1, "Left Window")
        self.left_win.refresh()

        self.right_win.clear()
        self.right_win.box()
        self.right_win.addstr(0, 1, title, curses.color_pair(2) | curses.A_BOLD)
        self.right_win.refresh()

    def render(self, title: str):
        while True:
            c = self.main_win.getch()
            if c == ord("q"):
                break
            elif c == curses.KEY_RESIZE:
                self.render_main_window(title)
                self.refresh_windows("hola")


    def cleanup(self):
        curses.endwin()

