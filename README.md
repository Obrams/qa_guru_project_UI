# UI test automation project for the "https://www.saucedemo.com/" demo online store
> www.saucedemo.com is a set of training pages that mimic an online store.

### Tech stack
<p  align="center">
  <code><img width="5%" title="Pycharm" src="images/logo/pycharm.png"></code>
  <code><img width="5%" title="Python" src="images/logo/python.png"></code>
  <code><img width="5%" title="Pytest" src="images/logo/pytest.png"></code>
  <code><img width="5%" title="Selene" src="images/logo/selene.png"></code>
  <code><img width="5%" title="Selenium" src="images/logo/selenium.png"></code>
  <code><img width="5%" title="GitHub" src="images/logo/github.png"></code>
  <code><img width="5%" title="Jenkins" src="images/logo/jenkins.png"></code>
  <code><img width="5%" title="Selenoid" src="images/logo/selenoid.png"></code>
  <code><img width="5%" title="Allure Report" src="images/logo/allure_report.png"></code>
  <code><img width="5%" title="Telegram" src="images/logo/tg.png"></code>
</p>

## Test coverage
- Successful login to the store.
- Login with empty fields.
- Login as a locked-out user.
- Login with invalid credentials.
- Adding an item to the cart.
- Removing an item from the cart.
- Checkout.


## Running tests
#### By default, all tests run remotely on Selenoid

### Local run
1. Clone the repository ($ git clone [Git repo](https://github.com/Obrams/qa_guru_project_UI))
2. Open the project in PyCharm
3. Run in the terminal
``` 
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest .
```

### Running tests in [Jenkins](https://jenkins.autotests.cloud/job/Ozerov_qa_quru_project_UI)
Click "Build Now"
<p><img src="images/screenshot/jenkins_job.png"></p>

For a remote run, add a build step in the **Build** section that creates/updates the .env file with your account data for <code>www.saucedemo.com</code>(**username_shop**, **password_shop**, **block_username_shop**, **block_password_shop**, **uncorrected_username_shop**, **uncorrected_password_shop**).

Example <code>.env</code> file in [Jenkins](https://jenkins.autotests.cloud/job/Ozerov_qa_quru_project_UI/configure)

<img src="images/screenshot/env.jpg"/>
Note: the credentials are test data.

### <img width="3%" title="Allure Report" src="images/logo/allure_report.png"> Allure test reports
#### For a local run:
Run in the terminal 
```
allure serve allure-results
``` 
#### For a Jenkins run
Click Allure Report or the report icon in a finished build
<p><img title="Jenkins_Allure" src="images/screenshot/jenkins_allure.png"></p>

### Test report examples
<img title="Allure_Report" src="images/screenshot/Allure Report0.png">
<img title="Allure_Example_Report" src="images/screenshot/Allure Report.png">

#### A video is attached to the report for every UI test
<img src="images/screenshot/video.gif">

### <p><img width="3%" title="Telegram" src="images/logo/tg.png"> Telegram</p>
<p>Test reports are sent to <a href='https://t.me/aqa_report_bot'>Telegram</a></p>
<img title="Telegram_report_screen" src="images/screenshot/telegram.png">
