from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    bmi = ''
    label = ''
    weight=''
    height=''
    if request.method == 'POST' and 'weight' in request.form:
        weight = float(request.form.get('weight'))
        height = float(request.form.get('height'))
        bmi = calc_bmi(weight, height)
        if bmi <=18.5:
            label="UnderWeight"
        elif bmi >= 18.5 and bmi <= 24.9:
            label = 'Normal weight'
        elif bmi>=25 and bmi<=30:
            label = "OverWeight"
        elif bmi>=30:
            label = "Obese"
        else:
            return "Error in BMI calculation!"
    return render_template("bmi_calc.html", weight=weight,height=height,bmi=bmi, label=label)

def calc_bmi(weight, height):
    return round((weight / ((height / 100) ** 2)), 2)

if __name__ == '__main__':
    app.run()
