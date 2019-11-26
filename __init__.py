from flask import Flask, render_template, request
import requests
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/enrich.db'
db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template("index.html")

# Routing
@app.route('/about/')
def about():
    return render_template("about.html")

@app.route('/hello/<name>')
def hello_world(name):
    return render_template("hello.html",
                            name=name)

@app.route('/gene_enrichment', methods=['GET', 'POST'])
@app.route('/gene_enrichment/<string:gene>')
def gene_enrichment(gene=None):
    genes=None
    if request.method == 'GET':
        gene=request.args.get('genes')
    elif request.method=='POST':
        gene=request.form.get('genes')
    if gene:
        genes = gene.split()
    return render_template("gene.html",
            genes=genes)