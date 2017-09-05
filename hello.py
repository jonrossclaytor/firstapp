
# coding: utf-8

# In[1]:

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return 'Hello, World'

if __name__ == '__main__':
    app.run(port=5000, debug=True)


# In[ ]:



