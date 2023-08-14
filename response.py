from flask import Flask,render_template

# Creating application instance
FAI=Flask(__name__)

# creating routing for view
@FAI.route('/temp')

# Creating view to render Html page as response
def temp():
    return render_template('temp.html',name='Narasimha',age=23)

# Running server
if __name__=='__main__':
    FAI.run(debug = True )
