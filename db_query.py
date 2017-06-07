import datetime
from models import orders, session


def get_order_waiting_time():
    first_unconfirmed_order = session.query(orders).filter(
                                                    orders.confirmed.is_(None)
                                                    ).order_by(
                                                    orders.created).first()
    time_delta = datetime.datetime.now() - first_unconfirmed_order.created
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
