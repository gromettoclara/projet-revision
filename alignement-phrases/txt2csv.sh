#!/bin/sh

TEXTFILES="textes"
REFERENCE="temoin.txt"
TMPDIR="/tmp/compare_phrases"
mkdir -p "$TMPDIR"

# Découpe le fichier témoin en phrases
awk 'BEGIN{RS="[.!?]"} {gsub(/\n/, " "); gsub(/^[ \t]+|[ \t]+$/, ""); print $0}' "$REFERENCE" > "$TMPDIR/temoin.txt"

# Liste des fichiers à comparer
FILES=""
for file in "$TEXTFILES"/*; do
    name=$(basename "$file")
    awk 'BEGIN{RS="[.!?]"} {gsub(/\n/, " "); gsub(/^[ \t]+|[ \t]+$/, ""); print $0}' "$file" > "$TMPDIR/$name"
    FILES="$FILES $name"
done

# En-tête CSV
echo -n "Phrase n°,Temoin" > resume_phrases.csv
for f in $FILES; do
    echo -n ",$f" >> resume_phrases.csv
done
echo "" >> resume_phrases.csv

# Comparaison phrase par phrase
i=1
while read ref; do
    echo -n "$i,\"$ref\"" >> resume_phrases.csv

    for f in $FILES; do
        phrase=$(sed -n "${i}p" "$TMPDIR/$f")
        if [ "$phrase" = "$ref" ]; then
            echo -n ",=" >> resume_phrases.csv
        else
            echo -n ",\"$phrase\"" >> resume_phrases.csv
        fi
    done

    echo "" >> resume_phrases.csv
    i=$((i + 1))
done < "$TMPDIR/temoin.txt"



