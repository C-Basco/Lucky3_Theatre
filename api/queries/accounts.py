from pydantic import BaseModel
from queries.pool import pool


class CustomerIn(BaseModel):
    email: str
    password: str
    first: str
    last: str


class CustomerOut(BaseModel):
    id: int
    email: str
    first: str
    last: str


class Customer(CustomerOut):
    hashed_password: str


class AccountQueries:
    def get_one(self, email: str) -> Customer:
        with pool.connection() as conn:
            with conn.cursor() as db:
                result = db.execute(
                    """
                          SELECT id,
                          email,
                          hashed_password,
                          first,
                          last
                          FROM users
                          WHERE email = %s;
                          """,
                    [email],
                )
                record = result.fetchone()
                print(record)
                return Customer(
                    id=record[0],
                    email=record[1],
                    hashed_password=record[2],
                    first=record[3],
                    last=record[4],
                )

    def get_all(self):
        with pool.connection() as conn:
            with conn.cursor() as db:
                result = db.execute(
                    """
                          SELECT id,
                          email,
                          first,
                          last
                          FROM users
                          """
                )
                customers = []
                for record in result:
                    customer = CustomerOut(
                        id=record[0],
                        email=record[1],
                        first=record[2],
                        last=record[3],
                    )
                    customers.append(customer)
                return customers

    def create_customer(
        self, customer: CustomerIn, hashed_password: str
    ) -> Customer:
        with pool.connection() as conn:
            with conn.cursor() as db:
                result = db.execute(
                    """
                          INSERT INTO users(email,
                          hashed_password,
                          first,
                          last)
                          VALUES(%s, %s, %s, %s)
                          RETURNING id, email,
                          hashed_password,
                          first,
                          last
                          """,
                    [
                        customer.email,
                        hashed_password,
                        customer.first,
                        customer.last,
                    ],
                )
                record = result.fetchone()
                customer = Customer(
                    id=record[0],
                    email=record[1],
                    hashed_password=record[2],
                    first=record[3],
                    last=record[4],
                )
                return customer
