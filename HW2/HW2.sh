echo "HW2 - Linux bash loops with Tucson Rain"

echo "_______________________________"
echo "Rows for months of 2021"
for month in {01..12}
do
	echo "For month ${month}, with Good data:"
	grep -w 2021-$month*.*Good tucson_rain.txt | wc -l
done

echo "_______________________________"
echo "Rows for months of 2020"
for month in {01..12}
do
	echo "For month ${month}, with Good data:"
	grep -w 2020-$month*.*Good tucson_rain.txt | wc -l
done

echo "_______________________________"
echo "Rows for months of 2019"
for month in {01..12}
do
	echo "Rows for month ${month}, with Good data:"
	grep -w 2019-${month}*.*Good tucson_rain.txt | wc -l
done
