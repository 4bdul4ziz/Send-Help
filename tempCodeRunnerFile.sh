read -p "Enter a Number:" n
echo -n "RESULT: "
if [ `expr $n % 2` == 0 ]
then
        echo "Even"
else
        echo "Odd"
fi
