from dotenv import dotenv_values


class Config:
    dotenv = dotenv_values()
    username_shop = dotenv.get('username_shop')
    password_shop = dotenv.get('password_shop')

    lock_username_shop = dotenv.get('block_username_shop')
    lock_password_shop = dotenv.get('block_password_shop')

    uncorrected_username_shop = dotenv.get('uncorrected_username_shop')
    uncorrected_password_shop = dotenv.get('uncorrected_password_shop')
