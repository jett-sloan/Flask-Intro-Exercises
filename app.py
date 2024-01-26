from flask import Flask, request
from python.operations import add, sub, mult, div

app = Flask(__name__)
print("HI!!!!")
# http://localhost:5000/add?a=10&b=20
#@app.route("/add")
#def add_args():
#    a = request.args.get('a')
#    b = request.args.get('b')
#    return add(a , b)
#
#@app.route("/sub")
#def sub_args():
#    a = request.args.get('a')
#    b = request.args.get('b')
#    return sub(a , b)
#
#@app.route("/mult")
#def mult_args():
#    a = request.args.get('a')
#    b = request.args.get('b')
#    return mult(a , b)
#
#@app.route("/div")
#def div_args():
#    a = request.args.get('a')
#    b = request.args.get('b')
#    return div(a , b)
#
#
#
operators = {
        "add": add,
        "sub": sub,
        "mult": mult,
        "div": div,
        }

@app.route("/math/<oper>")
def do_math(oper):
    """Do math on a and b."""

    a = request.args.get("a")
    b = request.args.get("b")
    if a is None or b is None:
        return "Must enter both 'a' and 'b' arguments."
    result = operators[oper](a, b)
    return str(result)
