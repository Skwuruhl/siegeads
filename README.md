# siegeads

Since Rainbow Six Siege lacks two sensitivity sliders for the different zoom levels I wrote a python script to somewhat get around that. The script calculates an XFactorAiming based on your FOV and other settings that will very accurately line up with two corresponding ADS sensitivity values. This is so that you can somewhat quickly change your sensitivity in-game based on if you're using an ACOG or not in the current round.

Zoom scales based on focal length and zoom ratio. Monitor distance is a bit more complicated.

Coefficient's function depends on the mode. In zoom it's a multiplier such that 1.3 is just a 1.3x multiplier to sensitivity. Monitor distance is vertical match distance where 100% is entered as 1.0. Don't use a value <= 0.

XFactorAiming value is set in Documents\\My Games\\Rainbow Six - Siege\\\<random shit\>\\GameSettings.ini under \[INPUT\]

As an example with my settings:

    FOV=70.53
    Mode ('zoom' or 'monitor distance')=zoom
    Coefficient=1

    ACOG ADS Sensitivity: 57
    Ironsight ADS Sensitivity: 94
    XFactorAiming=0.015511
    Glaz Scope Sensitivity: 57
    
After setting XFactorAiming in my config all I need to do in-game is set 57 ADS sensitivity when using an ACOG (or glaz scope) and 94 when using anything else.

