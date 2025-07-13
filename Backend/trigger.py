from pynput import mouse 
from pywinauto import application
from main import handle_word_trigger
import time
import main 

DOUBLE_TAP_TIME = 0.2

class DoubleTapListner:
    def __init__(self):
        self.last_click_time = 0
        self.listener = mouse.Listener(on_click=self.on_click)

    def on_click(self,x,y,button,pressed):
        if pressed:
            current_time = time.time()
            if current_time - self.last_click_time < DOUBLE_TAP_TIME:
                self.on_double_tap()
            self.last_click_time=current_time

    def on_double_tap(self):
        selected_text = self.get_selected_text()
        if selected_text:
            main.handle_word_trigger(selected_text)

    def get_selected_text(self):
        try:
            app = application().connect(title_re=".*")
            dlg=app.top_window()
            selected_text=dlg.Selection().window_text()
            return selected_text.strip()
        except Exception as e:
            print("Error Extracting select text:",e)
            return None
        
    def start(self):
        with self.listener:
            self.listener.join()


if __name__ == "__main__":
    listener = DoubleTapListner()
    listener.start()

    
