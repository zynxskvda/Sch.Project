@echo off
echo ---KALKULACKA---
:calc
set /p priklad=Zadej priklad: 
set vysledek=Error
set /a vysledek=%priklad%
echo Vysledek: %vysledek%
echo.
:znovu
set /p znovu=Dalsi priklad (y/n): 
if %znovu%==y echo. & goto calc
if %znovu%==n exit
echo Spatna odpoved
goto znovu
