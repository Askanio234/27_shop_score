import datetime
import os
from flask import Flask, render_template, request, send_from_directory
from db_query import get_order_waiting_time, get_unprocessed_orders, get_orders_processed_today

TODAY = datetime.date.today()

app = Flask(__name__)

@app.route('/')
def score():
    new_score = get_order_waiting_time()
    unprocessed_orders = get_unprocessed_orders()
    orders_today = get_orders_processed_today(TODAY)
    return render_template('score.html', score=new_score,
                            unconfirmed_orders=unprocessed_orders,
                            orders_confirmed=orders_today)


@app.route('/robots.txt')
def fetch_robots_txt():
    return send_from_directory(app.static_folder, request.path[1:])


if __name__ == "__main__":
    port = int(os.getenv("port", 5000))
    host = os.getenv("host", "0.0.0.0")
    app.run(host=host, port=port)
