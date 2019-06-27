exec_name=static_key_test
gcc -o $exec_name static.c
./$exec_name
rm $exec_name
