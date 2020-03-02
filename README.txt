Requires python3.

Usage :

% plot_counters.py rue_Jean_Martin.txt

or

% python visualise_consommations.py rue_Jean_Martin.txt

Sample data files:

  res_Valvert.txt
  
  rue_Jean_Martin.txt

Any counter series must be increasing (not strictly), unless the counter has been changed.  The program detects this and shifts older data for continuity with newer data (hence negative values are possible).

Missing data are possible.

Date cannot be duplicated (unless redress is not called).

Some default settings are in the file plot_counters.py.

Data file syntax:

*Column separator: \t (TAB) (can be customized).  Additional spaces are always permitted for better alignment in the text editor.

*First column must contain date in format YYYYMMDD.

*Above each column: subplot number or 0 to ignore columm.  Subplot will appear as 1, 2, 3...

*Any comment column must be ignored (with 0 on top).

*There must be a line beginning with end_of_python_code.  The text before this line will be executed as python code.  This is useful for settings.

Common errors:

*excess or lack of tabulation (check with Emacs whitespace-mode),

*wrong date like 20190229,

*duplicated date.

To do :

*interactive tool to get consumption rate on interval.


