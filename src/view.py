import curses

class View:
    def __init__(self, title: str, dirs):
        self.selected = 1
        self.main_win = curses.initscr()
        curses.curs_set(0)
        curses.start_color()
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_BLUE , curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_BLACK , curses.COLOR_BLUE)
        self.main_win.bkgd(curses.color_pair(1))

        self.render_main_window()
        self.title_main_window(title)
        self.refresh_windows()
        self.dirs_menu(dirs)

    def render_main_window(self):
        self.main_win.clear()
        self.main_win.box()
        #self.main_win.addstr(0, 1, title, curses.A_BOLD | curses.color_pair(2))
        self.main_win.refresh()

    def title_main_window(self, title: str):
        self.main_win.addstr(0, 1, title, curses.A_BOLD | curses.color_pair(2))
        self.main_win.refresh()

    def title_left_window(self, title: str):
        self.right_win.addstr(0, 1, title, curses.color_pair(2) | curses.A_BOLD)

    def refresh_windows(self):
        height, width = self.main_win.getmaxyx()
        window_height = height - 2
        window_width = width // 2

        self.left_win = self.main_win.subwin(window_height, window_width, 1, 0)
        self.right_win = self.main_win.subwin(window_height, window_width, 1, window_width)

        self.left_win.clear()
        self.left_win.box()

        self.left_win.refresh()

        self.right_win.clear()
        self.right_win.box()
        self.right_win.refresh()

    def dirs_menu(self, dirs):
        height, width = self.left_win.getmaxyx()
        if self.selected > height - 1:
            start_index = max(0, self.selected - height + 1)
        else:
            start_index = 0

        for i in range(start_index, height - 1):
            if i < len(dirs):
                if self.selected == i:
                    self.left_win.addstr(i - start_index + 1, 1, dirs[i], curses.color_pair(3))
                else:
                    self.left_win.addstr(i - start_index + 1, 1, dirs[i])
            else:
                break


        if self.selected >= height - 1:
            self.left_win.addstr(height - 1, 1, dirs[self.selected], curses.color_pair(3))

        self.left_win.refresh()




    def listener(self, c, dirs):
        if c == ord("j"):
            if self.selected > 0:
                self.selected -= 1
        elif c == ord("k"):
            if self.selected < len(dirs) - 1:
                self.selected += 1

    def cleanup(self):
        curses.endwin()

