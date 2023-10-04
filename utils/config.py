import os

import dotenv
from dotenv import dotenv_values


class Config:
    dotenv = dotenv_values()
    username_shop = dotenv.get('username_shop')
    password_shop = dotenv.get('password_shop')

    block_username_shop = dotenv.get('block_username_shop')
    block_password_shop = dotenv.get('block_password_shop')
