from flask import Flask, request
import json

app = Flask(__name__)


@app.route("/stockMock", methods=["GET", "POST"])
def stock():
    """
    接受股票ID，返回Mock的数据
    :param stockId: 股票id
    :return:
    """
    if request.method == 'POST':
        print(request.method)
        print(request.values.get('list'))
        key = request.values.get('list')
        if key == "gb_tsla":
            return "特斯拉,200,-0.12,2019-05-29 20:13:54,-0.1900,156.4000,157.0700,153.2200,211.7000,129.7700," \
                   "38602961,26667820,400029040000,5.01,30.90,0.00,0.00,0.00,0.00,2584000000,40.00,153.0000,-1.17,-1.81," \
                   "May 29 08:13AM EDT,May 28 04:01PM EDT,155.0000,29626.00"
        elif key == "rt_hk00700":
            return "XIAOMI-W,小米集团－Ｗ,9.840,9.950,9.940,9.800,9.920,-0.030,-0.302,9.910,9.920,286581930.310,29019956," \
                   "10.312,0.000,22.200,9.440,2019/05/29,16:08:08,100|0,N|N|Y,9.920|9.430|10.320,0|||0.000|0.000|0.000, |0,Y"
        else:
            raise ValueError

    else:
        print(request.method)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return "login"
    else:
        username = request.form.get('username')
        password = request.form.get('password')

        return "username: {0}，password：{1}".format(username, password)


@app.route('/logout', methods=['POST', 'GET'])
def logout():
    if request.method == 'GET':
        return "logout"


@app.route('/dosomething', methods=['POST', 'GET'])
def do_something():
    if request.method == 'GET':
        return "do something"


if __name__ == '__main__':
    app.run()