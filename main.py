from kivy.app import App
from kivy.uix.gridlayout import GridLayout


class Folkslayout(GridLayout):
    def claculate(self, calculation):
        if calculation:
            try:
                self.display.text = str(eval(calculation))
            except Exception:
                self.display.text = 'Error'


class FolksCalculatorApp(App):
    def build(self):
        return Folkslayout()


if __name__ == '__main__':
    FolksCalculatorApp().run()
