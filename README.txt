Requires python3.

Usage (in Unix shell for example) : 
% plot_counters.py rue_Jean_Martin.txt

Example input file: *.txt.
  
Example output graphics *.png.

Any counter series must be increasing (not strictly), unless the counter has been changed someday.  The program detects this and downshifts older data for continuity with newer data (hence negative values are possible), see redress.py.  A warning is printed for each downshift change.

Missing data are allowed (null in data file, yielding 'nan' in pandas DataFrame).

Some settings are in plot_counters.py.

Data file syntax:

* There must be a line beginning with end_of_python_code.  The text before this line will be executed as python code.  This is useful to pass file only settings.

* Column separator: \t (TAB) (can be set).  Additional spaces are always permitted for better alignment in the text editor.

* First column must contain date in format YYYYMMDD.

* On top of each column write subplot number (int >= 1) or 0 if not to plot (e. g. comments).  Subplots will appear as 1, 2, 3... from top to bottom.  

Common errors in data file:

* excess or lack of tabulation (check whitespace for example in Emacs with M-x whitespace-mode),

* wrong date,like 20190229,

* duplicated date.

A data file must remaining easy to read and write in text editor.

To do :

*Interactive tool for local linear fit and consumption rate determination.  No need of mathematics for linear interpolation:  it can be done by graphical interaction.

