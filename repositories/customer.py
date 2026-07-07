from repositories.base import BaseRepository
from models.customer import Customer


class CustomerRepository(BaseRepository[Customer]):

    def __init__(self):
        super().__init__(Customer)


customer_repository = CustomerRepository()