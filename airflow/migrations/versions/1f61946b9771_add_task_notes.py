#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

"""Add task notes

Revision ID: 1f61946b9771
Revises: c2c6eef5b00b
Create Date: 2021-12-18 13:58:08.604532

"""

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
from airflow.models.base import COLLATION_ARGS

revision = '1f61946b9771'
down_revision = 'c2c6eef5b00b'
branch_labels = None
depends_on = None


def upgrade():
    """Apply Add task notes"""
    """Apply Added event notes table"""
    op.create_table(
        'event_note',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('dag_id', sa.String(length=250, **COLLATION_ARGS), nullable=False),
        sa.Column('task_id', sa.String(length=250, **COLLATION_ARGS), nullable=True),
        sa.Column('execution_date', sa.DateTime(), nullable=False),
        sa.Column("event", sa.String(length=30), nullable=False),
        sa.Column('timestamp', sa.DateTime(), nullable=False),
        sa.Column('owner', sa.String(length=50), nullable=True),
        sa.Column('note', sa.Text(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
    )


def downgrade():
    """Unapply Add task notes"""
    op.drop_table('event_note')
