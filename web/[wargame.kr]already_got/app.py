from flask import Flask, make_response

app=Flask(__name__)

@app.route("/")
def hello():
    response=make_response("you've already got key! :p")
    response.headers['FLAG']='DH{You_C@n_Mak3_Cust0m_HTTP_Head3r}'
    return response

if __name__=='__main__':
    app.run(debug=False,host='0.0.0.0',port=5000)