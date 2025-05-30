from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, registry

table_registry = registry()


# Crie uma estrutura chamada dataclass (Classe de dados)
# classe que só tem atributos (classe de dados)
@table_registry.mapped_as_dataclass
class User:
    __tablename__ = 'users'

    # init significa que não será eu quem vai passar o campo ID.
    # SQLalchemy que vai incrementar
    # a partir do que o db der.
    # Primare_key já faz autoincrement por padrão.
    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    created_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now()
    )


@table_registry.mapped_as_dataclass
class Categoria:
    __tablename__ = 'categorias'

    categoria: Mapped[str] = mapped_column()


@table_registry.mapped_as_dataclass
class Post:
    texto: Mapped[str] = mapped_column()
    comentario: Mapped[str] = mapped_column()
    categoria: Mapped[Categoria] = mapped_column()
    curtidas: Mapped[int] = mapped_column()


@table_registry.mapped_as_dataclass
class Comentario:
    texto: Mapped[str] = mapped_column()
    post: Mapped[Post] = mapped_column()
    user: Mapped[User] = mapped_column()


@table_registry.mapped_as_dataclass
class Curtida:
    user: Mapped[User] = mapped_column()
    post: Mapped[Post] = mapped_column()
