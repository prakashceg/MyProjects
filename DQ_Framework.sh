cd /db_ap/db_ai/CheckFrmwork

export LD_LIBRARY_PATH=/u01/oracle/product/client1120/lib
export ORACLE_HOME=/u01/oracle/product/client1120

wfname=$1

echo "$wfname"

python2.7 /db_ap/db_ai/CheckFrmwork/CheckPy.py "$wfname">/bi_az/bi_ci/CheckFrmwork/log1.txt
