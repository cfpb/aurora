
PATH_OUTPUT=`env | grep PATH`
CHECK={{stattransfer_install_directory}}

if [[ "$PATH_OUTPUT" =~ "$CHECK" ]]
then
	echo "no need to add it"
else
	echo "need to add it"
	export PATH=$CHECK:$PATH
fi