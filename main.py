
from kivy.app import App
from kivy.uix.button import Button


class MyApp(App):
    def build(self):
        return Button(text = "Button",
                      font_size = 60,
                      on_press = self.btn_press,
                      background_color = [1,0,4,1])
    def btn_press(self, instance):
        print("clicked")
        instance.text = "Clicked"



if __name__ == "__main__":
    MyApp().run()
