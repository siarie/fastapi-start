from datetime import datetime
from sqlalchemy import Column, TIMESTAMP


class TimestampsMixin:
    __abstract__ = True

    __created_at_name__ = 'created_at'
    __updated_at_name__ = 'updated_at'
    __datetime_func__ = datetime.now()

    created_at = Column(
        __created_at_name__,
        TIMESTAMP(timezone=False),
        default=__datetime_func__,
        nullable=False
    )
    updated_at = Column(
        __updated_at_name__,
        TIMESTAMP(timezone=False),
        default=__datetime_func__,
        onupdate=__datetime_func__,
        nullable=False
    )
