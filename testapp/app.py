from flask import Flask, render_template, request, url_for, redirect, flash
app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.run(debug=True)

@app.route("/")
def home():
    return render_template("index.html")

# function to calculate the results of questions number 1
@app.route("/q1", methods=["GET"])
def q1():
    data = request.args
    error = ""
    message = "Lines are not overlapping"

    try:
        x1 = int(data["x1"])
        x2 = int(data["x2"])
        x3 = int(data["x3"])
        x4 = int(data["x4"])
        sep = ","   
        line1 = range((x2, x1) [x1 < x2], (x1+1, x2+1) [x1 < x2])
        line2 = range((x4, x3) [x3 < x4], (x3+1, x4+1) [x3 < x4])
        overlapping = [number for number in line1 if number in line2]
        if len(overlapping) > 0:
            message = "Lines are overlapping"
        return render_template('index.html', message=message)    
    except ValueError as v:
        error = getattr(v, 'message', repr(v))
        return render_template('index.html', error=error)
    except Exception as e:
        error = getattr(e, 'message', repr(e))
        return render_template('index.html', error=error)

# function to calculate the results of questions number 2
@app.route("/q2", methods=["GET"])
def q2():
    data = request.args
    if len(data) > 0:
        error = ""
        message = ""

        try:
            v1 = data["v1"]
            v2 = data["v2"]

            # check if values provided
            if len(v1) <= 0 or len(v2) <= 0:
                error = "Please provide versions"
                return render_template('q2.html', error=error)

            arr_v1 = v1.split(".")
            arr_v2 = v2.split(".")

            # check if both has same length
            if len(arr_v1) != len(arr_v2):
                error = "Please provide versions with same length"
                return render_template('q2.html', error=error)

            i = 0
            equal = 0
            
            while(i < len(arr_v1)): 
                if int(arr_v2[i]) > int(arr_v1[i]): 
                    message = "V1 is less than V2"        
                    break
                if int(arr_v1[i]) > int(arr_v2[i]): 
                    message = "V1 is greater than V2"
                    break
                if int(arr_v1[i]) == int(arr_v2[i]): 
                    equal += 1
                i += 1

            if equal == len(arr_v1):
                message = "V1 is equal to V2"
            return render_template('q2.html', message=message)    
        except ValueError as v:
            error = getattr(v, 'message', repr(v))
            return render_template('q2.html', error=error)
        except Exception as e:
            error = getattr(e, 'message', repr(e))
            return render_template('q2.html', error=error)
    else:
        return render_template('q2.html')