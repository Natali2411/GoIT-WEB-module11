"""make minor db upgrades part 2

Revision ID: 5e3c08af009b
Revises: e9fde4cd0689
Create Date: 2024-02-18 22:18:54.584858

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5e3c08af009b'
down_revision: Union[str, None] = 'e9fde4cd0689'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
