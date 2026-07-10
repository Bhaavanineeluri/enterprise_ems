from repositories.base import BaseRepository

from models.accounts_payable import AccountsPayable


accounts_payable_repository = BaseRepository(
    AccountsPayable
)