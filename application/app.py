from flask import Flask, render_template,request
app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def Home():
    num1 = request.form.get('num1')
    num2 = request.form.get('num2')
    
    operator = request.form.get('operator')
    

    if operator == '+':
        result = float(num1)+float(num2)
    elif operator == '-':
        result = float(num1) - float(num2)
    elif operator == '*':
        result = float(num1) * float(num2)
    elif operator == '/':
        result = float(num1) / float(num2)
    else:
        result = 'Invalid operator'

    return render_template("index.html", pagetitle="Home",result=result)


if __name__ == "__main__":
  app.run(debug=True, port=9000)