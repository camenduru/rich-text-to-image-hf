import gradio as gr


HTML = "<!-- Include stylesheet -->\n<link href=\"https://cdn.quilljs.com/1.3.6/quill.snow.css\" rel=\"stylesheet\">\n\n<!-- Create the editor container -->\n<div id=\"editor\">\n  <p>Hello World!</p>\n  <p>Some initial <strong>bold</strong> text</p>\n  <p><br></p>\n</div>\n\n<!-- Include the Quill library -->\n<script src=\"https://cdn.quilljs.com/1.3.6/quill.js\"></script>\n\n<!-- Initialize Quill editor -->\n<script>\n  var quill = new Quill('#editor', {\n    theme: 'snow'\n  });\n</script>"

def greet(name):
    return HTML, ''

iface = gr.Interface(fn=greet, gr.Textbox(placeholder="Enter sentence here..."), ["html", "json"])
iface.launch()