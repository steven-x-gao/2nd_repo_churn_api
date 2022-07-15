from flask import Flask, request,jsonify, render_template
import numpy as np
import gzip
import pickle

with gzip.open("ecom-user-churn.pgz", "r") as f:
	model_lrr = pickle.load(f)

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
	pred = ""
	if request.method == "POST":
		se_recency =request.form['se_recency']
		added_item_n = request.form['added_item_n']
		tse_len = request.form['tse_len']
		se_n = request.form['se_n']
		dt_flevent = request.form['dt_flevent']
		se_per_day = request.form['se_per_day']
		avg_atc_se = request.form['avg_atc_se']
		avg_se_len = request.form['avg_se_len']
		transid_n = request.form['transid_n']
		avg_ev_se = request.form['avg_ev_se']
		avg_itn_view = request.form['avg_itn_view']
		avg_itn_ev = request.form['avg_itn_ev']
		avg_itn_atc = request.form['avg_itn_atc']
		avg_transid_se = request.form['avg_transid_se']
		X = np.array([[float(se_recency), float(added_item_n), float(tse_len),
                       float(se_n), float(dt_flevent), float(se_per_day),
		       float(avg_atc_se), float(avg_se_len), float(transid_n),
                       float(avg_ev_se), float(avg_itn_view), float(avg_itn_ev),
                       float(avg_itn_atc), float(avg_transid_se)]])
		pred =model_lrr.predict_proba(X)[0][1]
		pred = round(pred,5)
	return render_template("index.html", pred=pred)


if __name__ == "__main__":
	app.run(debug=True, host='127.0.0.1', port=5000)

