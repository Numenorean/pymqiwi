Usage:
---------

Login with sms
~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: python

    import qiwimobile
    wallet = qiwimobile.MobileQIWI('380502153645', '2597') #phone & mobile_pin
    wallet.sendCode()
    wallet.login('7569')
    wallet.inputPin()
    
    
Login refresh token
~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: python

    import qiwimobile
    wallet = qiwimobile.MobileQIWI()
    wallet.refreshToken('1141a254525b1e1aca99297afc47f8d3', '2597') #refresh_token & mobile_pin
    

You can use token with qiwi api https://developer.qiwi.com/ru/qiwi-wallet-personal/
But token validity only 30 minutes, after this use refresh func
---------
