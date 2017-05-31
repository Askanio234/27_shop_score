import datetime
from models import orders, session


def get_last_order_waiting_time():
    last_order = session.query(orders).filter(
                                    orders.confirmed.isnot(None)).order_by(
                                    orders.id.desc()).first()
    time_delta = last_order.confirmed - last_order.created
    return round(time_delta.seconds/60, 1)


def get_unprocessed_orders():
    return session.query(orders).filter(orders.confirmed.is_(None)).count()


def get_orders_processed_today(today):
    today_start = datetime.datetime.combine(today,
                                            datetime.datetime.min.time())
    today_end = datetime.datetime.combine(today,
                                            datetime.datetime.max.time())
    return session.query(orders).filter(
                                orders.confirmed.between(
                                today_start, today_end)).count()

