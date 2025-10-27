from dotenv import load_dotenv
import os
import pytest
import playwright

load_dotenv()

@pytest.fixture(scope="session")
def sauce_base_url():
    return os.getenv("BASE_URL")

@pytest.fixture(scope="session")
def standard_username():
    return os.getenv("STANDARD_USERNAME")

@pytest.fixture(scope="session")
def secret_password():
    return os.getenv("SECRET_PASSWORD")

