import flet 
from flet import (
                UserControl,
                Page,
                Column,
                colors,
                Container,
                Row,
                border_radius,
                LinearGradient,
                alignment,
                Text,
                padding,
                ElevatedButton,
                FloatingActionButton
                
                )

class App(UserControl):
    def build(self):
        
        return Container(
            width=400,
            height= 400, 
            bgcolor= "black",
            gradient= LinearGradient(
                begin= alignment.bottom_left,
                end= alignment.top_right,
                colors= [ "",""]
                ),
            border_radius= border_radius.all(25),
        )
        
        
        
        return Column(
            controls= [
                Container(
                    width = 300,
                    height = 300,
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
                    # To add padding within the container, it must be done outside the content parameters
                    # padding = padding.all(50),
                    # If padding needs to be added to specific siddes, use the only() like with border radius
                    padding = padding.only(top=50,bottom=50),
                    content=
                    Column(
                        # Columns and Rows have no padding parameters at this moment, but they can be aligned
                        horizontal_alignment = "center",
                        # Spacing betweeen widgets can done using
                        spacing = 0,
                        controls = [
                            Row(
                                alignment = "center",
                                controls=[
                            Container(
                                width = 32,
                                height= 32,
                                bgcolor= "black",
                                border_radius= border_radius.all(25),
                            ),
                            Container(
                                width = 32,
                                height= 32,
                                bgcolor= "black",
                                border_radius= border_radius.all(25),
                            )]
                                ),
                            

                            Text(
                            # Text
                            "Hello World!",
                            # Size
                            size= 30,
                            # Weight
                            weight= "w900", # values of weight are from w100 - w900
                            # Color 
                            color = "black",
                            # Text align, center places it in the middle, start(all he way to the left) while end(to the right)
                            text_align= "center",
                            
                            ),
                        # To have multiple widgets in the container,we pass the widgets into a row or a column controls as the content can only take in one arguement
                            
                            Text(
                                # Text
                                "Hello World!",
                                # Size
                                size= 10,
                                # Weight
                                weight= "w900", # values of weight are from w100 - w900
                                # Color 
                                color = "black",
                                # Text align, center places it in the middle, start(all he way to the left) while end(to the right)
                                text_align= "center",
                            ),
                            # Buttons
                            # Buttons on flet are of different types with minor differences
                            Container(
                                
                            ElevatedButton(
                                text = 'Elevated Button',
                                # text color 
                                color = 'black',
                                # For an action when the button is clicked
                                on_click = lambda e:print("Hey!!"),
                                bgcolor= 'green',
                                height = 30
                            ),
                            padding = padding.only(top = 7,bottom = 7)
                            
                                ),
                            
                            # FloatingActionButton
                            FloatingActionButton(
                                text = " How Far!!! ",
                                width = 100,
                                height = 30,
                                bgcolor = "green",
                                color = 'black',
                                
                                ),
                            
                        ]
                    )
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