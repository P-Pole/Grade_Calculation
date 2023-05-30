from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['GET', 'POST'])
def calculate():
    if request.method == 'POST':
        UG_Project = float(request.form['UG_Project'])
        FL_Grades = [float(grade) for grade in request.form['FL_Grades'].split(",")]
        S_GRADES = [float(grade) for grade in request.form['S_GRADES'].split(",")]

        FL_Grades.sort()
        S_GRADES.sort()

        Calculation_One = UG_Project * 0.66666 + FL_Grades[0] * 0.33333
        Calculation_Two = (UG_Project * 0.66666 + FL_Grades[1] * 0.33333) * 0.666 + (S_GRADES[0] * 0.333 + S_GRADES[1] * 0.333 + S_GRADES[2] * 0.33333) * 0.333

        if Calculation_One >= Calculation_Two:
            final_grade = Calculation_One
        else:
            final_grade = Calculation_Two

        return render_template('result.html', final_grade=final_grade)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
