# Импорт всех классов
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

from kivy.core.window import Window

# Глобальные настройки
Window.size = (250, 200)
Window.clearcolor = (255 / 255, 186 / 255, 3 / 255, 1)
Window.title = "Конвертер"


class MyApp(App):

    # Создание всех виджетов (объектов)
    def __init__(self):
        super().__init__()
        self.label = Label(text='(a * b) mod c')
        self.answer = Label(text='результат mod c')
        #self.metres = Label(text='Метры')
        #self.santimetres = Label(text='Сантиметры')
        self.input_data = TextInput(hint_text='Введите значение (a)', multiline=False)
        self.input_data_b = TextInput(hint_text='Введите значение (b)', multiline=False)
        self.input_data_c = TextInput(hint_text='Введите значение (c)', multiline=False)
        self.input_data.bind(text=self.on_text)  # Добавляем обработчик события
        self.input_data_b.bind(text=self.on_text)  # Добавляем обработчик события
        self.input_data_c.bind(text=self.on_text)  # Добавляем обработчик события

    # Получаем данные и производит их конвертацию
    def on_text(self, *args):
        data = self.input_data.text
        data_b = self.input_data_b.text
        data_c = self.input_data_c.text
        if data.isnumeric():
            self.answer.text = 'По модулю C: ' + str((data * data_b) % data_c)
            #self.metres.text = 'Метры: ' + str(float(data) * 1000)
            #self.santimetres.text = 'Сантиметры: ' + str(float(data) * 100000)
        else:
            self.input_data.text = ''

    # Основной метод для построения программы
    def build(self):
        # Все объекты будем помещать в один общий слой
        box = BoxLayout(orientation='vertical')
        box.add_widget(self.label)
        box.add_widget(self.input_data)
        box.add_widget(self.input_data_b)
        box.add_widget(self.input_data_c)
        box.add_widget(self.answer)
        #box.add_widget(self.metres)
        #box.add_widget(self.santimetres)

        return box


# Запуск проекта
if __name__ == "__main__":
    MyApp().run()