from sqlalchemy import select

from Praticas_sala.ApiBlog.modelos import User


def test_create_user(session):
    user = User(username='George')

    session.add(user)
    session.commit()

    result = session.scalar(select(User).where(User.id == 1))

    assert result.username == 'George'
