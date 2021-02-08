from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)
dte = datetime.datetime.now()


num_b = 0

profileDB = {
    "success": True,
    "data": {
        "last_updated": "2/3/2021, 8:48:51",
        "username": "coolname",
        "role": "Engineer",
        "color": "#3478ff"
    }
}

tank = []


@app.route("/", methods=["GET"])
def home():
    return "hello lab 2"

# PROFILE Routes:
@app.route("/profile", methods=["GET", "POST", "PATCH"])
def profile():
    if request.method == "POST":
        # /POST
        profileDB["data"]["last_updated"] = (dte.strftime("%c"))
        profileDB["data"]["username"] = (request.json["username"])
        profileDB["data"]["role"] = (request.json["role"])
        profileDB["data"]["color"] = (request.json["color"])
       
        return jsonify(profileDB)
   
    elif request.method == "PATCH":
        # /PATCH
        profileDB["data"]["last_updated"] = (dte.strftime("%c"))
        
        tempDictionary = request.json
        a = tempDictionary.keys()
        
        for attribute in a:
            profileDB["data"][attribute] = tempDictionary[attribute]
  
        return jsonify(profileDB)

    else:
        # /GET
        return jsonify(profileDB)

# DATA Routes:
@app.route("/data", methods=["GET", "POST"])
def data():
    if request.method == "POST":
        # /POST
        global num_b
        num_b += 1   
        
        myPosts = {}
       
        myPosts["id"] = num_b
        myPosts["location"] = (request.json["location"])
        myPosts["lat"] = (request.json["lat"])
        myPosts["long"] = (request.json["long"])
        myPosts["percentage_full"] = (request.json["percentage_full"])

        tank.append(myPosts)

        return jsonify(tank)

    else:
        # /GET
        return jsonify(tank)

@app.route("/data/<int:tankID>", methods=["PATCH", "DELETE"])
def update(tankID):
     if request.method == "PATCH":
        # /PATCH
        for i in tank:
            if i["id"] == tankID:
                    tempDictionary = request.json
                    a = tempDictionary.keys()
        
                    for attribute in a:
                        index[attribute] = tempDictionary[attribute]
        
        return jsonify(tank) 

     elif request.method == "DELETE":
        # /DELETE
        for i in tank:
            if i["id"] == tankID:
                tank.remove(i)

        return jsonify(tank)

     else:
         # /GET
        return jsonify(tank)


if __name__ == '__main__':
   app.run(debug = True)