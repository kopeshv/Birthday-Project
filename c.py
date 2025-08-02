from flask import Flask,request,render_template
import os,datetime

web=Flask(__name__)
@web.route("/",methods=["POST","GET"])
def home():
    old=None
    k=None
    n=None
    day=None
    i=None
    p=None
    f=None
    if request.method=="POST":
        b_date=request.form.get("b_date","").strip().split("-")
        try:
            if len(b_date) !=3:
                raise ValueError ("date formate is worng")
            else:
                   
                b_d,b_m,b_y = map(int,b_date)
                today=datetime.date.today()
                birthday=datetime.date(b_y,b_m,b_d)
                old=today.year-b_y
                
                if (today.month,today.day)<(birthday.month,birthday.day):
                    old-=1
                    n=datetime.date(today.year,b_m,b_d)
                    day=(n-today).days 
                    
                
                elif (today.month,today.day)==(birthday.month,birthday.day):
                    i="Your Birthday is Today....."
                     
                else    :
                    n=datetime.date(today.year+1,b_m,b_d)
                    day=(n-today).days
                    p=datetime.date(today.year,b_m,b_d)
                    f=(today-p).days
                    i=f"it has been {f} days since your birthday had gone !" 
                           
                k=birthday.strftime("you were born in %A on %d %B %Y")    
                   
                    
                 
                    
        except Exception as e:
            old = f"Invalid input: {e}" 
        
                    
        
    return render_template("h.html",age=old,k=k,day=day,i=i)
if __name__=="__main__":
    web.run(debug=True)