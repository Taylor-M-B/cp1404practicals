from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabels(App):

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        # basic data example - dictionary of names: phone numbers
        # TODO: After running it, add another entry to the dictionary and see how the layout changes
        self.name_to_phone = ["Bob Brown", "Cat Cyan", "Oren Ochre"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Widgets"
        self.root = Builder.load_file('dynamic_widgets.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create buttons from dictionary entries and add them to the GUI."""
        for name in self.name_to_phone:
            # create a button for each data entry, specifying the text and id
            # (although text and id are the same in this case, you should see how this works)
            temp_label = Label(text=name, id=name)
            # add the button to the "entries_box" layout widget
            self.root.ids.entries_box.add_widget(temp_label)


DynamicLabels().run()
