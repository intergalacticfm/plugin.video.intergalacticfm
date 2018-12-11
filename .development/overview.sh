for i in ../resources/*-clearlogo.png; do
	convert -composite test.png $i -gravity center `basename $i`
done
./parse.py
markdown-pdf overview.md
