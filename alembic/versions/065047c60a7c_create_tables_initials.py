"""Create tables initials

Revision ID: 065047c60a7c
Revises: 
Create Date: 2024-05-16 00:00:13.916499

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '065047c60a7c'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "movies",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("title", sa.String),
        sa.Column("director", sa.String),
        sa.Column("genre", sa.String),
        sa.Column("year", sa.Integer)
    )
    op.create_table(
        "actores",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String),
        sa.Column("age", sa.Integer),
    )
    op.create_table(
        "actors_movies",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("actor_id", sa.Integer, sa.ForeignKey("actores.id")),
        sa.Column("movie_id", sa.Integer, sa.ForeignKey("movies.id")),
    )
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String),
        sa.Column("email", sa.String),
    )
    op.create_table(
        "user_rating_movies",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("user_id", sa.Integer, sa.ForeignKey("users.id")),
        sa.Column("movie_id", sa.Integer, sa.ForeignKey("movies.id")),
        sa.Column("rating", sa.Float),
    )
    op.create_table(
        "user_watched_movies",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("user_id", sa.Integer, sa.ForeignKey("users.id")),
        sa.Column("movie_id", sa.Integer, sa.ForeignKey("movies.id"))
    )

def downgrade() -> None:
    op.drop_table("user_watched_movies")
    op.drop_table("user_rating_movies")
    op.drop_table("users")
    op.drop_table("actors_movies")
    op.drop_table("actores")
    op.drop_table("movies")
