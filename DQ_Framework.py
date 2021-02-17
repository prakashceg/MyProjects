#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# -*- coding: utf-8 -*-
import cx_Oracle
import logging
import os
import sys
import re
import time
import pandas
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


wfname= sys.argv[1]
print wfname


server = 'mail.internal.salesforce.com'
server = smtplib.SMTP(server,25)
server.ehlo()
server.starttls()
msg = MIMEMultipart()
#msg['Subject'] = 'Table Data Issue Mail'
#msg = MIMEText('hello', 'html')
msg['Subject']='Table Data Issue Mail '+time.strftime("%d-%b-%Y")




def Fn_NullCheck(row_data,con):
                        #getresult='SELECT count(*) from '+str(row_data[2])+' Where '+str(row_data[3])+' IS NULL'
                        getresult='SELECT *  FROM (  SELECT count(*) NULL_ROW_COUNT FROM  '+str(row_data[2])+' Where '+str(row_data[3])+' is null  ) where NULL_ROW_COUNT>0'
                        global msg
                        curs_inner=con.cursor()
                        curs_inner.execute(getresult)
                        print(getresult)
                        qry=''
                        cnt=0
                        for cnt1 in curs_inner:
                                cnt=cnt1[0]
                        if cnt>0:
                                qry=qry+"insert into CTL_ERROR_TBL(QRY_DT ,QRY_ID ,CHECK_TYPE ,TBL_NAME,ERROR_COUNT , STOP_FLG) SELECT sysdate,"+str(row_data[0])+",'"+str(row_data[1])+"','"+str(row_data[2])+"',"+str(cnt)+",'"+ str(row_data[5])+"' from dual"
                                curs_inner.execute(qry)
                                curs_inner.execute("commit")
                        #echo -e "AWeb on `date -d "-1 days" +%Y-%m-%d`\nmessage date `date  +%Y-%m-%d`" | mailx -s "Webinar Automation Status Report"  pchokkalingam@salesforce.com
                        print(qry)
                        msg['Subject']='Table Data Issue Mail '+time.strftime("%d-%b-%Y")
                        msg='Test Query in Tbl_name='+str(row_data[2])+'  with Qry_Id ='+str(row_data[0])+' Failed'
                        mailto=str(row_data[10])
                        server.sendmail('pchokkalingam@salesforce.com',mailto,msg.as_string())








def Fn_UniqueCheck(row_data,con):
                        getresult='SELECT count(*)  FROM (  SELECT '+str(row_data[3])+',count(*)  FROM  '+str(row_data[2])+' group by  '+str(row_data[3])+' having count(*)>1 ) '
                        curs_inner=con.cursor()
                        curs_inner.execute(getresult)
                        print(getresult)
                        qry=''
                        cnt=0
                        for cnt1 in curs_inner:
                                cnt=cnt1[0]
                        if cnt>0:
                                qry=qry+"insert into CTL_ERROR_TBL(QRY_DT ,QRY_ID ,CHECK_TYPE ,TBL_NAME,ERROR_COUNT , STOP_FLG) SELECT sysdate,"+str(row_data[0])+",'"+str(row_data[1])+"','"+str(row_data[2])+"',"+str(cnt)+",'"+ str(row_data[5])+"' from dual"
                                curs_inner.execute(qry)
                                curs_inner.execute("commit")
                        print(qry)



def Fn_RefIntegrityCheck(row_data,con):
                        getresult=' select count(*)  from   '+str(row_data[2])+'  where  '+str(row_data[3])+'  not in ( select '+str(row_data[4])+' from '+str(row_data[15])+'  ) '
                        curs_inner=con.cursor()
                        curs_inner.execute(getresult)
                        print(getresult)
                        qry=''
                        cnt=0
                        for cnt1 in curs_inner:
                                cnt=cnt1[0]
                        if cnt>0:
                                qry=qry+"insert into CTL_ERROR_TBL(QRY_DT ,QRY_ID ,CHECK_TYPE ,TBL_NAME,ERROR_COUNT , STOP_FLG) SELECT sysdate,"+str(row_data[0])+",'"+str(row_data[1])+"','"+str(row_data[2])+"',"+str(cnt)+",'"+ str(row_data[5])+"' from dual"
                                curs_inner.execute(qry)
                                curs_inner.execute("commit")
                        print(qry)



def Fn_LengthCheck(row_data,con):
                        getresult=' select count(*)  from   '+str(row_data[2])+'  where  length('+str(row_data[3])+')<> '+str(row_data[4])
                        curs_inner=con.cursor()
                        curs_inner.execute(getresult)
                        print(getresult)
                        qry=''
                        cnt=0
                        for cnt1 in curs_inner:
                                cnt=cnt1[0]
                        if cnt>0:
                                qry=qry+"insert into CTL_ERROR_TBL(QRY_DT ,QRY_ID ,CHECK_TYPE ,TBL_NAME,ERROR_COUNT , STOP_FLG) SELECT sysdate,"+str(row_data[0])+",'"+str(row_data[1])+"','"+str(row_data[2])+"',"+str(cnt)+",'"+ str(row_data[5])+"' from dual"
                                curs_inner.execute(qry)
                                curs_inner.execute("commit")
                        print(qry)

def Fn_DistinctCheck(row_data,con):
                        getresult=' select count(*)  from   '+str(row_data[2])+'  where  '+str(row_data[3])+' not in ('+str(row_data[4])+') '
                        curs_inner=con.cursor()
                        curs_inner.execute(getresult)
                        print(getresult)
                        qry=''
                        cnt=0
                        for cnt1 in curs_inner:
                                cnt=cnt1[0]
                        if cnt>0:
                                qry=qry+"insert into CTL_ERROR_TBL(QRY_DT ,QRY_ID ,CHECK_TYPE ,TBL_NAME,ERROR_COUNT , STOP_FLG) SELECT sysdate,"+str(row_data[0])+",'"+str(row_data[1])+"','"+str(row_data[2])+"',"+str(cnt)+",'"+ str(row_data[5])+"' from dual"
                                curs_inner.execute(qry)
                                curs_inner.execute("commit")
                        print(qry)

def Fn_Business_Rule_Check(row_data,con):
                        getresult= str(row_data[4])
                        curs_inner=con.cursor()
                        curs_inner.execute(getresult)
                        print(getresult)
                        qry=''
                        cnt=0
                        for cnt1 in curs_inner:
                                cnt=cnt1[0]
                        if cnt>0:
                                qry=qry+"insert into CTL_ERROR_TBL(QRY_DT ,QRY_ID ,CHECK_TYPE ,TBL_NAME,ERROR_COUNT , STOP_FLG) SELECT sysdate,"+str(row_data[0])+",'"+str(row_data[1])+"','"+str(row_data[2])+"',"+str(cnt)+",'"+ str(row_data[5])+"' from dual"
                                curs_inner.execute(qry)
                                curs_inner.execute("commit")
                        print(qry)

def Fn_Load_Miss_Check(row_data,con):
                        getresult=' select count(*)  from   '+str(row_data[2])+'  where  '+str(row_data[3])+' not in ('+str(row_data[4])+') '
                        curs_inner=con.cursor()
                        curs_inner.execute(getresult)
                        print(getresult)
                        qry=''
                        cnt=0
                        for cnt1 in curs_inner:
                                cnt=cnt1[0]
                        if cnt>0:
                                qry=qry+"insert into CTL_ERROR_TBL(QRY_DT ,QRY_ID ,CHECK_TYPE ,TBL_NAME,ERROR_COUNT , STOP_FLG) SELECT sysdate,"+str(row_data[0])+",'"+str(row_data[1])+"','"+str(row_data[2])+"',"+str(cnt)+",'"+ str(row_data[5])+"' from dual"
                                curs_inner.execute(qry)
                                curs_inner.execute("commit")
                        print(qry)


#orcl = cx_Oracle.connect(con)
if __name__ == "__main__":


        logging.basicConfig(level=logging.INFO)
        logger = logging.getLogger(__name__)
        user = "ci_projects"
        host = "db-azprd.internal.salesforce.com"
        port = "1531"
        sid = "azprd"

        pswd = "20170918_Ci_Projects"

        con = cx_Oracle.connect (user, pswd, 'db-azprd.internal.salesforce.com:1531/azprd_bu')
        pswd = "20170918_Ci_Projects"

          # Build connection string

        curs = con.cursor()
        curs_inner=con.cursor()
        printHeader = True # include column headers in each table output

        sql = "select * from CTL_QC_TBL WHERE WF_NAME='"+wfname+"'" # get a list of all tables
        curs.execute(sql)
        logger.info('Start reading database')
        ExpectedQuery=''
        ActualQuery=''
        for row_data in curs:
                if(row_data[1]=="NULL"):
                        Fn_NullCheck(row_data,con)

                if(row_data[1]=="UNIQUE"):
                        Fn_UniqueCheck(row_data,con)

                if(row_data[1]=="REF_INTEGRITY"):
                        Fn_RefIntegrityCheck(row_data,con)

                if(row_data[1]=="LENGTH"):
                        Fn_LengthCheck(row_data,con)

                if(row_data[1]=="DISTINCT"):
                        Fn_DistinctCheck(row_data,con)


                if(row_data[1]=="BUSINESS_RULE"):
                        Fn_Business_Rule_Check(row_data,con)

                if(row_data[1]=="LOAD_MISS"):
                        Fn_Load_Miss_Check(row_data,con)


server.quit()

