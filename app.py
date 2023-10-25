from flask import Flask,request,render_template,redirect,url_for

app = Flask(__name__)
@app.route('/success/<int:score>')
def success(score):
    return "Congratulations!! you are passed and your score is " + str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "Better luck next time! your score is " + str(score)



@app.route('/calculator',methods=['POST','GET'])
def calculator():
    if request.method=='GET':
        return render_template('calculator.html')
    
    else:
        maths=float(request.form['maths'])
        science=float(request.form['science'])
        history=float(request.form['history'])
        
        average_marks=(maths+science+history)/3
        result=''
        if average_marks>=50:
            result='success'
            
        else:
            result='fail'
            
        return redirect(url_for(result,score= average_marks))
        
       # return render_template('result.html',results=average_marks)
    
    
    

    


if __name__=='__main__':
    app.run(debug=True)
     
    

