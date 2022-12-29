import flet 
from flet import  UserControl,Page,Column,colors,Container,Row,border_radius,LinearGradient,alignment,Text


class App(UserControl):
    def build(self):
        return Column(
            controls= [
                Container(
                    width = 200,
                    height = 200,
                    bgcolor = colors.AMBER_300,
                    # The .all() method rounds all sides of the container.
                    # border_radius= border_radius.all(25),
                    # The .only() method applies the radius selectively to the side desired.
                    border_radius= border_radius.only(topRight=25, bottomLeft=25),
                    # To add gradient to the container
                    gradient=LinearGradient(
                        begin = alignment.bottom_right,
                        end= alignment.top_left,
                        colors=[colors.AMBER_200, colors.TEAL_300]
                        ),
                     # To add other widgets inside the container, use the contents parameter
                     content=
                         Text(
                    #         # Text
                             "Hello World!",
                    #         # Size
                             size= 55,
                    #         # Weight
                             weight= "w900", # values of weight are from w100 - w900
                    #         # Color 
                             color = "black",
                            
                            ),
                    
                        
                    
                    
                ),
                
                
                
                
                
                
                
                
            ]
        )
    
    
    
def main(page: Page):
    
    # set the title of the window
    page.title = "Flet Tutorial"
    
    # set the width of the window
    page.window_width = 600
    page.window_height = 300
    
    # to change color 
    page.bgcolor = colors.BLUE_GREY_500
    
    
    
    # to disable resizing 
    # page.window_resizable = False
    
    page.update()
    
    app = App()
    page.add(app)





if __name__ == "__main__":
    flet.app(target = main)