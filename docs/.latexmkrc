# =====================================================================
#  .latexmkrc
# =====================================================================

$pdf_mode    = 1;          # produce PDF with pdflatex
$bibtex_use  = 2;          # run bibtex when needed, and clean its output
$out_dir     = 'build';    # every output, including the PDF, goes to build/
$aux_dir     = 'build';    # keep aux files with the rest

# Do not stop and wait for input on an error; the log tells the story.
$pdflatex = 'pdflatex -interaction=nonstopmode -synctex=1 -file-line-error %O %S';

# latexmk -c also removes these
$clean_ext = 'synctex.gz run.xml bbl bcf fdb_latexmk fls figlist auxlock';

# Build this one when latexmk is called with no file name.
@default_files = ('emmanuel_dataTerra_Report1-MOD-Cheatsheet.tex');
