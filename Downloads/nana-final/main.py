from flask import Flask, render_template, request
from extractors.remoteok import extract_remoteok_jobs
from extractors.wwr import extract_wwr_jobs

app = Flask("jobScrapper")


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    remoteok = extract_remoteok_jobs(keyword)
    wwr = extract_wwr_jobs(keyword)
    jobs = remoteok + wwr
    return render_template("search.html", keyword=keyword, jobs=jobs)


app.run("0.0.0.0")
