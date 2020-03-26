
PATH_OUTPUT=`env | grep PATH`
CHECK={{stattransfer_install_directory}}

if [[ ! "$PATH_OUTPUT" =~ "$CHECK" ]]
then
	export PATH=$CHECK:$PATH
fi
