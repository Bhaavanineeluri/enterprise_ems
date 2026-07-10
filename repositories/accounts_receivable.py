from repositories.base import BaseRepository

from models.accounts_receivable import AccountsReceivable


accounts_receivable_repository = BaseRepository(
    AccountsReceivable
)