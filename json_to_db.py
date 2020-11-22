# -*- coding: utf-8 -*-
import json
import MySQLdb

def read_file(f='./pythonstudy/denis_automation_tasks_closed_by_sa.json'):
    with open(f, encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data

if __name__ == "__main__":
    data=read_file(f='./pythonstudy/xag_1')['records']
    db=MySQLdb.connect(host="mariadb",user="pi",passwd="JuveLivorno01",db="snowdata",use_unicode=True,charset="utf8")
    c=db.cursor()
    A=[]
    [A.append(tuple(x.values())) for x in data]
    error_count=0
    for x in A:

#        sql="""insert into incident_cmdb_tasks (number, cmdb_ci, sys_class_name) values('%s','%s','%s')"""%x[:-1]

#        sql="""insert into c_tasks (number, opened_at, parent,\
#        u_automation, closed_at, assignment_group, cmdb_ci, sc_catalog,\
#        sys_class_name, closed_by) \
#        values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"""%x[:-1]

#        sql="""insert into tasks (number, parent_sys_class_name,\
#        closed_at, assignment_group, sys_created_on, approval, parent_number,\
#        active, sys_class_name, assigned_to ,closed_by, automation_flag) \
#        values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','M')"""%x[:-1]

#        sql="""insert into system_id (number, sys_id) values('%s','%s')"""%x[:2]
        sql="""insert into system_c_tasks_activity (fieldname, newvalue, sys_created_on, documentkey, record_checkpoint, user, oldvalue) \
values("%s","%s","%s","%s","%s","%s","%s")"""%(x[0],x[1].replace('\r','').replace('\n','').replace('\"','').replace('\'',''),*x[2:6],x[6].replace('\r','').replace('\n','').replace('\"','').replace('\'',''))

#        sql="""insert into system_problems_activity (fieldname, sys_id, newvalue, sys_created_on, documentkey, tablename, record_checkpoint, user, oldvalue, sys_created_by) \
#values("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")"""%(*x[:2],x[2].replace('\r','').replace('\n','').replace('\"','').replace('\'',''),*x[3:8],x[8].replace('\r','').replace('\n','').replace('\"','').replace('\'',''),x[9])
        try:
            c.execute(sql)
        except MySQLdb.Error as e:
            error_count+=1
            print(e)
            print(sql)
        except TypeError as e:
            error_count+=1
            print(e)
            print(sql)
        except ValueError as e:
            error_count+=1
            print(e)
            print(sql)
    db.commit()
    c.close()
    db.close()
    print(error_count)
