# Importing libraries
from fasthtml.common import *
import string
import secrets

# Defining the FastHTML app
app = FastHTML(
    hdrs=(
        # Add Tailwind CSS
        Script(src="https://cdn.tailwindcss.com"),
    )
)


@app.route('/')
def home():
    title = "Password Generator - With FastHTML"
    form = Form(
        Input(id="length_input", type="number", placeholder="Enter the length",
              cls="border-2 border-gray-400 rounded-md p-2"),
        Button("Generate", cls="bg-slate-900 text-white p-2 rounded-md mt-2"),
        cls="flex flex-col items-center mt-10",
        hx_post="/generate",
        target_id="result",
        hx_swap="innerHTML"
    )
    result = Div(id="result", cls="text-center mt-10")

    return Title(title), Main(H1(title, cls="text-3xl text-center mt-10"), form, result)


alph = string.ascii_letters + string.digits + string.punctuation


@app.route("/generate")
def post(length_input: int):
    length = length_input
    if length < 8:
        return "Password length should be greater than 8 characters"
    password = ''.join(secrets.choice(alph) for i in range(length))
    return password


if '__main__' == __name__:
    serve()
