from flask import Flask,render_template,request
import datetime,time,os
web=Flask(__name__)

@web.route("/",methods=["POST","GET"])

def home():
    date=None
    detail=None
    age=None
    remain=None
    msg=None
    left=None
    topic=None
    sec=None
    if request.method=="POST":
        B_date=request.form.get("b_date","").strip()
        b_date=B_date.split("-")
        timu=request.form.get("timu","").strip()
        today=datetime.date.today()
        
        try:
            topic="✨.....YOUR DETAILS.....✨"
            if len(b_date)!=3:
                raise ValueError ("❌...Given Birthday Date Was Wrong ❗ ")
            else:
                if timu:
                    dt=f"{timu} {B_date}"
                    stu=time.strptime(dt,"%H:%M:%S %d-%m-%Y")
                    b_second=time.mktime(stu)
                    l_t=time.localtime()
                    l_second=time.mktime(l_t)
                    sec=int(l_second-b_second)
                    
                    
                b_d,b_m,b_y=map(int,b_date)
                birthday=datetime.date(b_y,b_m,b_d)
                date=birthday.strftime("%d-%m-%Y")
                detail=birthday.strftime("You Were Born On %A On %d %B %Y")
                age=(today.year-birthday.year)
                if (birthday.month,birthday.day)>(today.month,today.day):
                    age-=1
                    new=datetime.date(today.year,b_m,b_d)
                    remain=(new-today).days
                elif     (birthday.month,birthday.day)==(today.month,today.day):
                    msg="✨...Today is Your Birthday...💫...Wish You Happy Birthday Dear...🥳"
                elif  (birthday.month,birthday.day)<(today.month,today.day):
                       new=datetime.date(today.year+1,b_m,b_d)
                       remain=(new-today).days
                       new1=datetime.date(today.year,b_m,b_d)
                       left=(today-new1).days  
        except Exception as e:
            topic=f"Ivalid Input : {e}" 
    return render_template("h.html",topic=topic,date=date,left=left,age=age,remain=remain,msg=msg,detail=detail,sec=sec)                      
                       
                    

port = int(os.environ.get("PORT", 10000))
web.run(host="0.0.0.0", port=port)