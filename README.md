# siegeads

Since Rainbow Six Siege lacks two sensitivity sliders for the different zoom levels I wrote a python script to somewhat get around that. The script calculates an XFactorAiming based on your FOV and desired vertical match distance that will very accurately line up with two corresponding ADS sensitivity values. This is so that you can somewhat quickly change your sensitivity in-game based on if you're using an ACOG or not in the current round.

Coefficient is vertical match distance where 100% is entered as 1.0

XFactorAiming value is set in Documents\\My Games\\Rainbow Six - Siege\\\<random shit\>\\GameSettings.ini under \[INPUT\]

As an example with my settings:

    FOV=70.53
    Coefficient=0
    
    ACOG ADS Sensitivity: 57
    Ironsight ADS Sensitivity: 94
    XFactorAiming=0.015511
    
After setting XFactorAiming in my config all I need to do in-game is set 57 ADS sensitivity when using an ACOG and 94 when using anything else.

