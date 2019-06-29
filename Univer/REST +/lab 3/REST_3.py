from flask import Flask, jsonify, request

app = Flask(__name__)

applications = [

]

plans =[

]


def groupsFormat():
    numb = plans[-1]["app"]
    for i in applications:
        if(i['number']==numb):
            plans[-1]["app"] = i
    return jsonify(plans[-1])

#Wellcome pages----------------------------------------------------------------
@app.route("/",methods=["GET"])
def wellcome():
    return "Вітаємо в системі житлово-комунального підприємства!\n\n"+"Щоб увійти як користувач скористайтесь тегом '\\user'\n"+"Щоб увійти як адміністратор скористайтесь тегом '\\admin'\n\n"+"Для перегляду заявок скористайтесь тегом '\\applications'\n"+"Для перегляду планів робіт скористайтесь тегом '\\plans'"

@app.route("/user",methods=["GET"])
def user():
    return "Вітаємо в системі житлово-комунального підприємства!\n\n"+"Для написання заявки скористайтесь тегом POST '\\user\\write'\n"+"1. У заявці потрібно вказати імя (параметр 'name')\n"+"2. Вид робіт('type')\n3. Масштаб робіт ('value')\n"+"4.Час робіт('time)'\n\n"+"Для перегляду заявок скористайтесь тегом '\\applications'\n"+"Для перегляду планів робіт скористайтесь тегом '\\plans'"

@app.route("/admin",methods=["GET"])
def admin():
    return "Вітаємо в системі житлово-комунального підприємства!\n\n"+"Для перегляду заявок скористайтесь тегом '\\applications'\n"+"Для написання плану робіт скористайтесь тегом POST '\\admin\\write'\n"+"1. У плані потрібно вказати дату (параметр 'date')\n"+"2. Кількість виділених людей ('numb')\n3.  Інструменти ('tools')\n"+"4. Номер заявки('app')\n"+"5. Вартість('Value')\n\n"+"Для перегляду планів робіт скористайтесь тегом '\\plans'"

#Дістаємо заявки---------------------------------------------------------------
@app.route("/applications",methods=["GET"])
def getApplications():
    return jsonify(applications)

@app.route("/applications/<id>",methods=["GET"])
def getApplication(id):
    id = int(id)-1
    return jsonify(applications[id])

#Дістаємо плани робіт----------------------------------------------------------
@app.route("/plans",methods=["GET"])
def getPlans():
    return jsonify(plans)

@app.route("/plans/<id>",methods=["GET"])
def getPlan(id):
    id = int(id)-1
    return jsonify(plans[id])

#Створюємо заявки--------------------------------------------------------------
@app.route("/user/write",methods=["POST"])
def addApplication():
    name = request.json['name']
    type = request.json['type']
    value = request.json['value']
    time = request.json['time']
    number = len(applications)
    if(number>0):
        number = applications[-1]['number']+1
    data = {'number':number,'name':name,'type':type,'value':value,'time':time}
    applications.append(data)
    return jsonify(data)

#Створюємо план--------------------------------------------------------------
@app.route("/admin/write",methods=["POST"])
def addPlan():
    date = request.json['date']
    numb = int(request.json['numb'])
    tools = request.json['tools']
    value = float(request.json['value'])
    app = int(request.json['app'])

    id = len(plans)
    if(id>0):
        id = plans[-1]['id']+1

    data = {'date':date,'numb':numb,'tools':tools,'value':value,'app':app,'id':id}
    plans.append(data)

    plan = groupsFormat()

    return plan #jsonify(data)

#Видаляємо Заявку---------------------------------------------------------------
@app.route("/applications/<id>",methods=["DELETE"])
def deleteApplication(id):
    id = int(id)
    app =  -1
    for a in applications:
        if (a["number"] == id):
            app = a
            break
    if(app==-1):
        return "No account found"

    applications.remove(app)
    return jsonify(app)

#Видаляємо План---------------------------------------------------------------
@app.route("/plans/<id>",methods=["DELETE"])
def deletePlan(id):
    id = int(id)
    pl =  -1
    for p in plans:
        if (p["id"] == id):
            pl = p
            break
    if(pl==-1):
        return "No account found"

    plans.remove(pl)
    return jsonify(pl)

if __name__ == "__main__":
    app.run(port = 5000)
