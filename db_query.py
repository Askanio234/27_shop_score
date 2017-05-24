import datetime
from models import Orders, session


TODAY = datetime.date.today()


def get_last_order_waiting_time():
    last_order = session.query(Orders).filter(
                                    Orders.confirmed.isnot(None)).order_by(
                                    Orders.id.desc()).first()
    time_delta = last_order.confirmed - last_order.created
    return round(time_delta.seconds/60)


def get_unprocessed_orders():
    return session.query(Orders).filter(Orders.confirmed.is_(None)).count()


def get_orders_processed_today(today):
    today_start = datetime.datetime.combine(today,
                                            datetime.datetime.min.time())
    today_end = datetime.datetime.combine(today,
                                            datetime.datetime.max.time())
    return session.query(Orders).filter(
                                Orders.confirmed.between(
                                today_start, today_end)).count()

