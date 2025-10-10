from guizero import App, Text, TextBox, PushButton, Box, info

# main app
app = App(title="learning gui system", width=500, height=400, layout="auto")

# header
header = Text(app, text="my learning gui", size=20, font="Arial", color="blue")

# text area
text_box = TextBox(app, multiline=True, width=50, height=10)

# input field
entry = TextBox(app, width=30)
entry.value = "type something here"

# button functions
def say_hello():
    user_text = entry.value
    text_box.value += f"hello, {user_text}!\n"

def clear_text():
    text_box.value = ""

# buttons
button_box = Box(app, layout="grid")

hello_btn = PushButton(button_box, text="say hello", command=say_hello, grid=[0,0])
clear_btn = PushButton(button_box, text="clear", command=clear_text, grid=[1,0])

app.display()