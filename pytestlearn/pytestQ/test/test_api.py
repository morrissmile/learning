import sys
sys.path.append('../code')
import signapi
# from code import signapi

class Test_for_pytest:

    def test_signin_api(self):
        account1 = signapi.Login('morris.lin+pro7@taroko.io', 'a12345678')
        loginmail = account1.signinapi()
        assert 'morris.lin+pro7@taroko.io' == loginmail


