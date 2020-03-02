Requires python3.

Usage (in Unix shell for example) : 
% plot_counters.py rue_Jean_Martin.txt

Example input data file: *.txt.
  
Example output graphics file *.png.

Any counter series must be increasing (not strictly), unless the counter is changed some day.  The program detects this and downshifts older data for continuity with newer data (hence negative values are possible on plot).  A warning is printed for each downshift, so that the user has a chance to check if the non increasing series is his own error in copying data rather than actual counter change.

Missing data (void in data file) are allowed (yielding 'nan' in pandas DataFrame).

Some default settings are in plot_counters.py.

Data file syntax:

* There must be a line beginning with 'end_of_python_code'.  The text before this line will be executed as python code.  This is useful for file settings (overriding defaults).

* Column separator: TAB (sep='\t').  Additional spaces are permitted for better alignment in text editor.

* First column must contain date in format YYYYMMDD.

* On top of each column (except the first) must be subplot number (int >= 1) or 0 if not to plot (e. g. comments).  Subplots will appear in this order from top to bottom.  

Common errors in data file:

* excess or lack of tabulation (check whitespace for example in Emacs with M-x whitespace-mode),

* wrong date,like 20190229,

* duplicated date.

Data file must remain readable and writable with only text editor.

To do :

*Interactive tool for local linear fit and consumption rate determination.  No need of mathematics for linear interpolation:  it can be done by graphical interaction.

