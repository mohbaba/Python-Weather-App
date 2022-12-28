import flet 
from flet import  UserControl,Page,Column


class App(UserControl):
    def build(self):
        return Column()
    
    
    
def main(page: Page):
    
    # set the title of the window
    page.title = "Flet Tutorial"
    
    # set the width of the window
    page.window_width = 600
    page.window_height = 300
    
    
    # to disable resizing 
    page.window_resizable = False
    
    page.update()
    
    app = App()
    page.add(app)





if __name__ == "__main__":
    flet.app(target = main)