Usage:
---------

Login with sms
~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: python

    import qiwimobile
    wallet = qiwimobile.MobileQIWI('380502153645', '2597') # phone & mobile_pin
    wallet.sendCode()
    wallet.login('7569') # code from sms
    wallet.inputPin()
    
    
Login refresh token
~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: python

    import qiwimobile
    wallet = qiwimobile.MobileQIWI()
    wallet.refreshToken('1141a254525b1e1aca99297afc47f8d3', '2597') # refresh_token from func 'inputPin' & mobile_pin
    

You can use token with qiwi api https://developer.qiwi.com/ru/qiwi-wallet-personal/
----------------
Token valid only 30 minutes, after use refresh func
----------------
