from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.properties import ObjectProperty


class TodoScreen(BoxLayout):
    task_input = ObjectProperty(None)
    task_container = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(TodoScreen, self).__init__(**kwargs)
        self.to_do_list = []

    def add_task(self):
        task_text = self.task_input.text.strip()
        if task_text:
            # Add to our internal list
            self.to_do_list.append(task_text)

            # Create a task item layout
            task_layout = BoxLayout(
                orientation='horizontal',
                size_hint_y=None,
                height=dp(40)
            )

            # Task label
            task_label = Label(
                text=task_text,
                halign='left',
                valign='middle',
                size_hint_x=0.8,
                text_size=(dp(200), dp(40))
            )

            # Delete button
            delete_button = Button(
                text='X',
                size_hint_x=0.2
            )
            # Store the task text with the button for reference when deleting
            delete_button.task_text = task_text
            delete_button.bind(on_press=self.delete_task)

            # Add widgets to task layout
            task_layout.add_widget(task_label)
            task_layout.add_widget(delete_button)

            # Add the task layout to the container
            self.task_container.add_widget(task_layout)

            # Clear the input field
            self.task_input.text = ''

    def delete_task(self, instance):
        # Remove from internal list
        if instance.task_text in self.to_do_list:
            self.to_do_list.remove(instance.task_text)

        # Remove from UI
        # We need to find the parent layout of the button (which is the task_layout)
        task_layout = instance.parent
        self.task_container.remove_widget(task_layout)


class Main(App):
    def build(self):
        # Set window size for testing on desktop
        # This won't affect mobile deployment
        Window.size = (300, 500)

        return TodoScreen()


if __name__ == '__main__':
    Main().run()